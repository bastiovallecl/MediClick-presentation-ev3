<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import * as THREE from 'three'
import { EffectComposer } from 'three/addons/postprocessing/EffectComposer.js'
import { RenderPass } from 'three/addons/postprocessing/RenderPass.js'
import { UnrealBloomPass } from 'three/addons/postprocessing/UnrealBloomPass.js'

const container = ref(null)
let scene, camera, renderer, composer, animationId
let particlesMesh, dnaGroup, crossGroup, pillGroup

onMounted(() => {
  if (!container.value) return

  // 1. Scene Setup
  scene = new THREE.Scene()
  
  // 2. Camera Setup
  camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 1000)
  camera.position.z = 40

  // 3. Renderer Setup
  renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true, powerPreference: "high-performance" })
  renderer.setSize(window.innerWidth, window.innerHeight)
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
  renderer.toneMapping = THREE.ACESFilmicToneMapping
  renderer.toneMappingExposure = 1.2
  container.value.appendChild(renderer.domElement)

  // 4. Background Particles (Data flow)
  const particlesGeometry = new THREE.BufferGeometry()
  const particlesCount = 2000
  const posArray = new Float32Array(particlesCount * 3)
  const colorsArray = new Float32Array(particlesCount * 3)
  const color1 = new THREE.Color(0x0ea5e9)
  const color2 = new THREE.Color(0xc084fc)
  
  for(let i = 0; i < particlesCount; i++) {
    const r = 20 + Math.random() * 40
    const theta = Math.random() * Math.PI * 2
    const phi = Math.acos(Math.random() * 2 - 1)
    
    posArray[i*3] = r * Math.sin(phi) * Math.cos(theta)
    posArray[i*3+1] = r * Math.sin(phi) * Math.sin(theta)
    posArray[i*3+2] = r * Math.cos(phi)

    const mixedColor = color1.clone().lerp(color2, Math.random())
    colorsArray[i*3] = mixedColor.r
    colorsArray[i*3+1] = mixedColor.g
    colorsArray[i*3+2] = mixedColor.b
  }
  
  particlesGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3))
  particlesGeometry.setAttribute('color', new THREE.BufferAttribute(colorsArray, 3))
  const particlesMaterial = new THREE.PointsMaterial({
    size: 0.15,
    vertexColors: true,
    transparent: true,
    opacity: 0.5,
    blending: THREE.AdditiveBlending
  })
  particlesMesh = new THREE.Points(particlesGeometry, particlesMaterial)
  scene.add(particlesMesh)

  // 5. Medical Elements
  
  // A. DNA Helix
  dnaGroup = new THREE.Group()
  const sphereGeo = new THREE.SphereGeometry(0.4, 16, 16)
  const cylinderGeo = new THREE.CylinderGeometry(0.1, 0.1, 3.5, 8)
  const blueMat = new THREE.MeshStandardMaterial({ color: 0x0ea5e9, emissive: 0x0ea5e9, emissiveIntensity: 0.6 })
  const purpleMat = new THREE.MeshStandardMaterial({ color: 0xc084fc, emissive: 0xc084fc, emissiveIntensity: 0.6 })
  const linkMat = new THREE.MeshStandardMaterial({ color: 0xffffff, transparent: true, opacity: 0.3 })

  const strandsCount = 30
  for(let i=0; i<strandsCount; i++) {
    const y = (i - strandsCount/2) * 1.2
    const angle = i * 0.4
    
    const s1 = new THREE.Mesh(sphereGeo, blueMat)
    s1.position.set(Math.cos(angle)*3, y, Math.sin(angle)*3)
    dnaGroup.add(s1)
    
    const s2 = new THREE.Mesh(sphereGeo, purpleMat)
    s2.position.set(Math.cos(angle+Math.PI)*3, y, Math.sin(angle+Math.PI)*3)
    dnaGroup.add(s2)

    const link = new THREE.Mesh(cylinderGeo, linkMat)
    link.position.set(0, y, 0)
    link.rotation.y = -angle
    link.rotation.z = Math.PI / 2
    dnaGroup.add(link)
  }
  dnaGroup.position.set(-20, 0, -10)
  dnaGroup.rotation.z = Math.PI / 6
  scene.add(dnaGroup)

  // B. Medical Crosses
  crossGroup = new THREE.Group()
  const boxGeo1 = new THREE.BoxGeometry(0.8, 2.4, 0.8)
  const boxGeo2 = new THREE.BoxGeometry(2.4, 0.8, 0.8)
  const crossMat = new THREE.MeshStandardMaterial({ color: 0x10b981, emissive: 0x10b981, emissiveIntensity: 0.4 }) // Emerald
  
  for(let i=0; i<10; i++) {
    const cross = new THREE.Group()
    cross.add(new THREE.Mesh(boxGeo1, crossMat))
    cross.add(new THREE.Mesh(boxGeo2, crossMat))
    cross.position.set((Math.random()-0.5)*60, (Math.random()-0.5)*40, (Math.random()-0.5)*30 - 15)
    cross.rotation.set(Math.random()*Math.PI, Math.random()*Math.PI, Math.random()*Math.PI)
    cross.userData = { rx: (Math.random()-0.5)*0.02, ry: (Math.random()-0.5)*0.02 }
    crossGroup.add(cross)
  }
  scene.add(crossGroup)

  // C. Medical Pills (Capsules)
  pillGroup = new THREE.Group()
  const capsuleGeo = new THREE.CapsuleGeometry(0.5, 1.2, 4, 16)
  const pillMat = new THREE.MeshStandardMaterial({ color: 0xffffff, emissive: 0x3b82f6, emissiveIntensity: 0.3 })
  for(let i=0; i<15; i++) {
    const pill = new THREE.Mesh(capsuleGeo, pillMat)
    pill.position.set((Math.random()-0.5)*60, (Math.random()-0.5)*40, (Math.random()-0.5)*30 - 15)
    pill.rotation.set(Math.random()*Math.PI, Math.random()*Math.PI, Math.random()*Math.PI)
    pill.userData = { rx: (Math.random()-0.5)*0.03, ry: (Math.random()-0.5)*0.03 }
    pillGroup.add(pill)
  }
  scene.add(pillGroup)


  // 6. Lights
  const ambientLight = new THREE.AmbientLight(0xffffff, 0.3)
  scene.add(ambientLight)
  const pointLight = new THREE.PointLight(0x38bdf8, 2, 100)
  pointLight.position.set(0, 10, 10)
  scene.add(pointLight)

  // 7. Post-Processing (Bloom)
  const renderScene = new RenderPass(scene, camera)
  const bloomPass = new UnrealBloomPass(new THREE.Vector2(window.innerWidth, window.innerHeight), 1.2, 0.4, 0.85)
  bloomPass.threshold = 0.2
  bloomPass.strength = 1.0
  bloomPass.radius = 0.5

  composer = new EffectComposer(renderer)
  composer.addPass(renderScene)
  composer.addPass(bloomPass)

  // 8. Mouse interaction
  let mouseX = 0
  let mouseY = 0
  const windowHalfX = window.innerWidth / 2
  const windowHalfY = window.innerHeight / 2

  const onDocumentMouseMove = (event) => {
    mouseX = (event.clientX - windowHalfX) * 0.002
    mouseY = (event.clientY - windowHalfY) * 0.002
  }
  document.addEventListener('mousemove', onDocumentMouseMove)

  // 9. Animation Loop
  const tick = () => {
    const elapsedTime = performance.now() * 0.001

    // DNA Rotation
    dnaGroup.rotation.y = elapsedTime * 0.2

    // Crosses Rotation
    crossGroup.children.forEach(cross => {
      cross.rotation.x += cross.userData.rx
      cross.rotation.y += cross.userData.ry
    })

    // Pills Rotation
    pillGroup.children.forEach(pill => {
      pill.rotation.x += pill.userData.rx
      pill.rotation.y += pill.userData.ry
    })

    particlesMesh.rotation.y = elapsedTime * 0.03

    // Parallax effect with mouse
    camera.position.x += (mouseX * 5 - camera.position.x) * 0.05
    camera.position.y += (-mouseY * 5 - camera.position.y) * 0.05
    camera.lookAt(scene.position)

    composer.render()
    animationId = requestAnimationFrame(tick)
  }
  tick()

  // 10. Handle Resize
  const handleResize = () => {
    camera.aspect = window.innerWidth / window.innerHeight
    camera.updateProjectionMatrix()
    renderer.setSize(window.innerWidth, window.innerHeight)
    composer.setSize(window.innerWidth, window.innerHeight)
  }
  window.addEventListener('resize', handleResize)

  // Cleanup
  onUnmounted(() => {
    document.removeEventListener('mousemove', onDocumentMouseMove)
    window.removeEventListener('resize', handleResize)
    cancelAnimationFrame(animationId)
    if(container.value && renderer.domElement) {
      container.value.removeChild(renderer.domElement)
    }
    renderer.dispose()
  })
})
</script>

<template>
  <div ref="container" class="three-d-container"></div>
</template>

<style scoped>
.three-d-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: -1;
  pointer-events: none;
  overflow: hidden;
  background: radial-gradient(circle at center, rgba(11, 17, 32, 0.4) 0%, rgba(11, 17, 32, 0.9) 100%);
}
</style>
