---
theme: seriph
colorSchema: dark
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## MediClick Presentation
  Sistema Inteligente de Gestión y Distribución de Medicamentos.
drawings:
  persist: false
transition: zoom-3d
title: MediClick - HealthTech Platform
fonts:
  sans: 'Plus Jakarta Sans'
  serif: 'Outfit'
  mono: 'Fira Code'
---

<div class="flex justify-center mb-3 z-10 relative">
  <img src="/Logo_VG_blanco.png" alt="Logo Institución" class="h-9 object-contain opacity-70" />
</div>

<div class="glass-panel p-8 max-w-2xl mx-auto relative z-10">
<div class="flex justify-center mb-4">
  <img src="/logo_nuevo.png" alt="MediClick Logo" class="h-24 object-contain hover:scale-105 transition-transform duration-500" />
</div>

<h1 class="text-4xl font-black text-white mb-3">
  MediClick
</h1>

<h2 class="text-white/80 text-xl font-bold tracking-tight leading-snug">
  Sistema Inteligente de Gestión y Distribución de Medicamentos
</h2>

<p class="text-white/40 mt-3 text-sm font-light">
  Para Pacientes de Zonas Rurales y Personas con Movilidad Reducida.
</p>

<div class="mt-5 pt-4 border-t border-white/10 text-center">
  <p class="text-white/35 font-semibold tracking-[0.14em] uppercase" style="font-size:0.5rem">Formulación de Proyectos Informáticos</p>
  <p class="text-white/25 mt-1" style="font-size:0.55rem">Rafael Navarrete &nbsp;·&nbsp; Bastián Ovalle &nbsp;·&nbsp; Adriel Troncoso</p>
</div>
</div>

---
layout: default
class: bg-grid
transition: cube-left
---

# Acto 1: El Problema

<div class="grid grid-cols-2 gap-6 mt-4">
<div class="glass-panel p-5 v-click" v-motion :initial="{ opacity: 0, x: -50 }" :enter="{ opacity: 1, x: 0, transition: { duration: 800 } }">
  <h3 class="text-lg font-bold text-white mb-4 flex items-center gap-2">
    <carbon-warning-alt class="text-red-500" /> Brecha de Acceso
  </h3>
  <ul class="space-y-3 text-slate-300 text-sm">
    <li class="flex gap-2">
      <carbon-close-outline class="text-cyan-400 mt-0.5 shrink-0" />
      <span>Pacientes rurales deben viajar horas para retirar sus medicamentos en el CESFAM.</span>
    </li>
    <li class="flex gap-2">
      <carbon-close-outline class="text-cyan-400 mt-0.5 shrink-0" />
      <span>Personas con movilidad reducida dependen de terceros.</span>
    </li>
    <li class="flex gap-2 text-red-400 font-bold mt-4 text-base">
      <carbon-chart-line-data class="shrink-0" />
      <span>Alto riesgo de abandono del tratamiento (No adherencia).</span>
    </li>
  </ul>
</div>

<div class="relative rounded-2xl overflow-hidden shadow-[0_20px_50px_rgba(0,0,0,0.5)] glow-box v-click" v-motion :initial="{ opacity: 0, x: 50 }" :enter="{ opacity: 1, x: 0, transition: { duration: 800, delay: 300 } }">
  <img src="/rural_patient.png" class="absolute inset-0 w-full h-full object-cover opacity-70" />
  <div class="absolute inset-0 bg-gradient-to-t from-[#0b1120] via-[#0b1120]/40 to-transparent"></div>
  <div class="absolute bottom-4 left-4 right-4">
    <p class="text-base italic text-white font-serif leading-normal">"La tecnología debe acercar la salud a quienes más lo necesitan, no alejarla."</p>
  </div>
</div>
</div>

---
layout: default
class: bg-grid
transition: cube-left
---

# Contexto, Objetivo y Alcance

<div class="grid grid-cols-3 gap-4 mt-4">

<div class="glass-panel p-3 v-click border-l-4 border-red-400">
  <h3 class="text-red-400 text-sm font-bold mb-2 flex items-center gap-2">
    <carbon-warning-alt /> Contexto
  </h3>
  <p class="text-slate-300 text-xs leading-normal">
    En Chile, más de <span class="text-white font-bold">2 millones de personas</span> viven en zonas rurales o tienen movilidad reducida. Actualmente deben trasladarse al CESFAM para retirar sus medicamentos, lo que provoca <span class="text-red-400 font-semibold">abandono de tratamientos crónicos, reingresos hospitalarios evitables</span> y sobrecarga en los centros de salud.
  </p>
</div>

<div class="glass-panel p-3 v-click border-l-4 border-cyan-400">
  <h3 class="text-cyan-400 text-sm font-bold mb-2 flex items-center gap-2">
    <carbon-flag /> Objetivo
  </h3>
  <p class="text-slate-300 text-xs leading-normal">
    <span class="text-white font-bold">Desarrollar</span> un sistema digital integrado que automatice la gestión de recetas médicas y la distribución de medicamentos a domicilio, reduciendo en al menos un <span class="text-cyan-400 font-bold">60% el tiempo de acceso</span> al tratamiento para pacientes de difícil alcance.
  </p>
</div>

<div class="glass-panel p-3 v-click border-l-4 border-purple-400">
  <h3 class="text-purple-400 text-sm font-bold mb-2 flex items-center gap-2">
    <carbon-list /> Alcance
  </h3>
  <ul class="text-slate-300 text-xs space-y-1.5 leading-normal">
    <li class="flex gap-1.5"><carbon-checkmark class="text-green-400 mt-0.5 shrink-0"/><span>Módulos: gestión de recetas, despacho, seguimiento y notificaciones</span></li>
    <li class="flex gap-1.5"><carbon-checkmark class="text-green-400 mt-0.5 shrink-0"/><span>Integración con CESFAM y farmacias piloto</span></li>
    <li class="flex gap-1.5"><carbon-checkmark class="text-green-400 mt-0.5 shrink-0"/><span>Hasta 5.000 usuarios en fase piloto</span></li>
    <li class="flex gap-1.5"><carbon-close class="text-red-400 mt-0.5 shrink-0"/><span class="text-slate-500">No incluye fabricación ni dispensación autónoma</span></li>
    <li class="flex gap-1.5"><carbon-close class="text-red-400 mt-0.5 shrink-0"/><span class="text-slate-500">No incluye integración con seguros privados</span></li>
  </ul>
</div>

</div>

<p class="mt-4 text-center text-slate-500 text-xs v-click">
  Tipo de proyecto: <span class="text-cyan-400 font-bold">Desarrollo de Software</span> · Modalidad: <span class="text-blue-400 font-bold">Cloud-Native</span>
</p>

---
layout: center
class: text-center
transition: flip-y
---

<h1 class="text-4xl font-black text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-blue-600 mb-4">
  Acto 2: La Solución
</h1>

<p class="mt-4 text-xl text-slate-300 font-light tracking-wide" v-click>
  Un ecosistema digital integrado y automatizado.
</p>

---
layout: default
transition: cube-left
---

# Flujo Operativo Inteligente

<div class="mt-4 glass-panel p-5 rounded-2xl v-click glow-box">

```mermaid
sequenceDiagram
    autonumber
    
    actor Paciente as 🧑‍🦱 Paciente
    participant MediClick as 💻 MediClick AI
    participant CESFAM as 🏥 CESFAM
    participant Farmacia as 💊 Farmacia
    participant Distrib as 🚚 Distribución

    rect rgba(6, 182, 212, 0.1)
    note right of Paciente: 📱 Fase 1: Solicitud y Validación
    Paciente->>+MediClick: Solicita o confirma receta médica
    MediClick->>+CESFAM: Valida receta e identidad
    CESFAM-->>-MediClick: Aprobación y datos de receta
    end

    rect rgba(59, 130, 246, 0.1)
    note right of MediClick: 🧠 Fase 2: IA y Logística
    MediClick->>+Farmacia: Revisa inventario y reserva
    Farmacia-->>-MediClick: Medicamentos preparados
    MediClick->>+Distrib: Asigna ruta priorizada (IA)
    end
    
    rect rgba(139, 92, 246, 0.1)
    note right of Distrib: 📍 Fase 3: Última Milla
    Distrib->>+Paciente: Entrega y confirmación biométrica
    Distrib-->>-MediClick: Notificación de entrega exitosa
    MediClick->>-Paciente: Recordatorio automático de tratamiento
    end
```

</div>

<p class="text-center text-cyan-400 mt-3 v-click text-xs font-medium">
  * El sistema prioriza automáticamente según urgencia médica, ubicación y condiciones de almacenamiento.
</p>

---
layout: two-cols
class: bg-grid
transition: wheel-rotate
---

# Acto 3: Inteligencia Artificial

<div class="pr-6 mt-1">
<div class="space-y-3">
  <div class="glass-panel p-3.5 v-click transition-transform hover:scale-105">
    <h3 class="text-cyan-400 text-sm font-bold flex items-center gap-2 mb-1.5">
      <carbon-chart-evaluation /> Predicción de Demanda
    </h3>
    <p class="text-xs leading-snug text-slate-300">Modelos de Machine Learning anticipan escasez de stock basándose en temporalidad e historial.</p>
  </div>
  
  <div class="glass-panel p-3.5 v-click transition-transform hover:scale-105">
    <h3 class="text-blue-400 text-sm font-bold flex items-center gap-2 mb-1.5">
      <carbon-map /> Priorización de Entregas
    </h3>
    <p class="text-xs leading-snug text-slate-300">Algoritmos de enrutamiento optimizan la logística considerando caminos rurales y urgencia.</p>
  </div>

  <div class="glass-panel p-3.5 v-click transition-transform hover:scale-105">
    <h3 class="text-purple-400 text-sm font-bold flex items-center gap-2 mb-1.5">
      <carbon-notification /> Recordatorios Inteligentes
    </h3>
    <p class="text-xs leading-snug text-slate-300">NLP para enviar notificaciones personalizadas vía WhatsApp/SMS para asegurar adherencia.</p>
  </div>
</div>
</div>

::right::

<div class="h-full flex items-center justify-center pl-4 v-click" v-motion :initial="{ scale: 0.8, opacity: 0 }" :enter="{ scale: 1, opacity: 1, transition: { duration: 600 } }">
<div class="relative w-full rounded-2xl overflow-hidden shadow-[0_0_40px_rgba(14,165,233,0.4)] glow-box border border-slate-700">
  <img src="/ai_dashboard_pro.png" class="w-full object-cover" />
</div>
</div>

---
layout: center
class: text-center
transition: slide-up
---

<h1 class="text-5xl font-black text-white mb-10 drop-shadow-[0_0_20px_rgba(255,255,255,0.3)]">
  Acto 4: Alternativas de Solución
</h1>

<div class="grid grid-cols-2 gap-8 w-full max-w-4xl mx-auto">
  <div class="glass-panel p-8 relative overflow-hidden transition-all duration-500 transform" :class="$slidev.nav.clicks === 1 ? 'scale-110 border-blue-400 shadow-[0_0_40px_rgba(96,165,250,0.6)] z-10' : 'scale-100 border-slate-700 hover:border-blue-500/50'">
    <div class="absolute inset-0 bg-blue-500/20 opacity-0 transition-opacity duration-500" :class="$slidev.nav.clicks === 1 ? 'opacity-100' : ''"></div>
    <h3 class="text-3xl font-black text-blue-400 mb-3 relative z-10">Alternativa 1</h3>
    <p class="text-xl text-white font-medium relative z-10">Desarrollo Propio Cloud-Native</p>
  </div>
  
  <div class="glass-panel p-8 border border-slate-700 opacity-60 transition-all duration-500">
    <h3 class="text-3xl font-bold text-slate-400 mb-3">Alternativa 2</h3>
    <p class="text-xl text-slate-300 font-medium">Microsoft Power Platform</p>
  </div>
</div>

<v-click />

---
layout: center
transition: zoom
---

<div class="glass-panel p-6 relative overflow-hidden group w-full max-w-2xl glow-box">
<div class="absolute top-0 right-0 w-40 h-40 bg-blue-500 rounded-full blur-[80px] opacity-20 group-hover:opacity-40 transition-opacity"></div>

<h3 class="text-xl font-bold text-white mb-1">Alternativa 1</h3>
<h4 class="text-blue-400 text-2xl font-black mb-5">Desarrollo Propio Cloud-Native</h4>

<div class="flex gap-4 mb-5 justify-center">
  <logos-vue class="text-3xl drop-shadow-lg hover:scale-110 transition-transform" />
  <logos-django-icon class="text-3xl drop-shadow-lg hover:scale-110 transition-transform" />
  <logos-postgresql class="text-3xl drop-shadow-lg hover:scale-110 transition-transform" />
  <logos-docker-icon class="text-3xl drop-shadow-lg hover:scale-110 transition-transform" />
  <logos-aws class="text-3xl drop-shadow-lg hover:scale-110 transition-transform" />
</div>

<ul class="space-y-3 text-sm text-slate-200 text-left pl-4">
  <li class="flex items-center gap-3 text-green-400"><carbon-checkmark/> <span class="text-slate-200">Máximo control, flexibilidad y escalabilidad.</span></li>
  <li class="flex items-center gap-3 text-green-400"><carbon-checkmark/> <span class="text-slate-200">IA e integraciones totalmente personalizadas.</span></li>
  <li class="flex items-center gap-3 text-green-400"><carbon-checkmark/> <span class="text-slate-200">Sin licencias por usuario — menor costo operacional a largo plazo.</span></li>
  <li class="flex items-center gap-3 text-red-400 mt-3"><carbon-close/> <span class="text-slate-400">Mayor inversión y tiempo de desarrollo inicial.</span></li>
</ul>
</div>

---
layout: center
class: text-center
transition: slide-up
---

<h1 class="text-5xl font-black text-white mb-10 drop-shadow-[0_0_20px_rgba(255,255,255,0.3)]">
  Acto 4: Alternativas de Solución
</h1>

<div class="grid grid-cols-2 gap-8 w-full max-w-4xl mx-auto">
  <div class="glass-panel p-8 border border-slate-700 opacity-50 transition-all duration-500">
    <h3 class="text-3xl font-black text-slate-500 mb-3 flex justify-center items-center gap-2">
      <carbon-checkmark class="text-green-500" /> Alternativa 1
    </h3>
    <p class="text-xl text-slate-400 font-medium">Desarrollo Propio Cloud-Native</p>
  </div>
  
  <div class="glass-panel p-8 relative overflow-hidden transition-all duration-500 transform" :class="$slidev.nav.clicks === 1 ? 'scale-110 border-cyan-400 shadow-[0_0_40px_rgba(6,182,212,0.6)] z-10' : 'scale-100 border-slate-700 hover:border-cyan-500/50'">
    <div class="absolute inset-0 bg-cyan-500/20 opacity-0 transition-opacity duration-500" :class="$slidev.nav.clicks === 1 ? 'opacity-100' : ''"></div>
    <h3 class="text-3xl font-bold text-cyan-400 mb-3 relative z-10">Alternativa 2</h3>
    <p class="text-xl text-white font-medium relative z-10">Microsoft Power Platform</p>
  </div>
</div>

<v-click />

---
layout: center
transition: zoom
---

<div class="glass-panel p-6 relative overflow-hidden group w-full max-w-2xl glow-box">
<div class="absolute top-0 left-0 w-40 h-40 bg-cyan-500 rounded-full blur-[80px] opacity-20 group-hover:opacity-40 transition-opacity"></div>

<h3 class="text-xl font-bold text-white mb-1">Alternativa 2</h3>
<h4 class="text-cyan-400 text-2xl font-black mb-5">Microsoft Power Platform</h4>

<div class="flex gap-5 mb-5 justify-center">
  <logos-microsoft class="text-3xl drop-shadow-lg hover:scale-110 transition-transform" />
  <logos-microsoft-azure class="text-3xl drop-shadow-lg hover:scale-110 transition-transform" />
  <vscode-icons-file-type-excel class="text-3xl drop-shadow-lg hover:scale-110 transition-transform" />
</div>

<ul class="space-y-3 text-sm text-slate-200 text-left pl-4">
  <li class="flex items-center gap-3 text-green-400"><carbon-checkmark/> <span class="text-slate-200">Despliegue rápido — funcional en semanas.</span></li>
  <li class="flex items-center gap-3 text-green-400"><carbon-checkmark/> <span class="text-slate-200">Menor riesgo técnico y curva de aprendizaje baja.</span></li>
  <li class="flex items-center gap-3 text-red-400 mt-3"><carbon-close/> <span class="text-slate-400">Flexibilidad limitada (Vendor lock-in con Microsoft).</span></li>
  <li class="flex items-center gap-3 text-red-400"><carbon-close/> <span class="text-slate-400">Costos de licenciamiento recurrentes elevados.</span></li>
</ul>
</div>

---
layout: default
transition: flip-y
---

# Acto 5: Evaluación Cualitativa de Eficiencia

<p class="text-slate-400 text-xs mb-3">Escala 1 (menor eficiencia) → 5 (mayor eficiencia) · Puntaje P = suma de los 4 atributos</p>

<div class="glass-panel overflow-hidden border border-slate-700/50 v-click">
<table class="w-full text-left border-collapse text-xs">
  <thead>
    <tr class="bg-slate-800/90 text-white">
      <th class="p-3 border-b border-slate-700 text-sm">Atributo de Eficiencia</th>
      <th class="p-3 border-b border-slate-700 text-center text-slate-400 text-xs font-normal">Descripción</th>
      <th class="p-3 border-b border-slate-700 text-center text-blue-400 font-bold text-xs">Alt. 1<br/><span class="font-normal">Desarrollo Propio</span></th>
      <th class="p-3 border-b border-slate-700 text-center text-cyan-400 font-bold text-xs">Alt. 2<br/><span class="font-normal">Power Platform</span></th>
    </tr>
  </thead>
  <tbody class="text-slate-200">
    <tr class="hover:bg-white/5 transition-colors v-click">
      <td class="p-3 border-b border-slate-800 font-semibold text-sm">🎯 Efectividad</td>
      <td class="p-3 border-b border-slate-800 text-slate-400 text-xs">¿Qué tanto cumple los objetivos del proyecto?</td>
      <td class="p-3 border-b border-slate-800 text-center"><span class="bg-blue-500/20 text-blue-300 px-3 py-1 rounded-full font-black text-base border border-blue-500/30">5</span></td>
      <td class="p-3 border-b border-slate-800 text-center"><span class="bg-slate-500/20 text-slate-300 px-3 py-1 rounded-full font-black text-base border border-slate-500/30">3</span></td>
    </tr>
    <tr class="hover:bg-white/5 transition-colors v-click">
      <td class="p-3 border-b border-slate-800 font-semibold text-sm">💻 Plataforma Tecnológica</td>
      <td class="p-3 border-b border-slate-800 text-slate-400 text-xs">¿Qué tan adecuada y actualizada es la tecnología?</td>
      <td class="p-3 border-b border-slate-800 text-center"><span class="bg-blue-500/20 text-blue-300 px-3 py-1 rounded-full font-black text-base border border-blue-500/30">5</span></td>
      <td class="p-3 border-b border-slate-800 text-center"><span class="bg-slate-500/20 text-slate-300 px-3 py-1 rounded-full font-black text-base border border-slate-500/30">3</span></td>
    </tr>
    <tr class="hover:bg-white/5 transition-colors v-click">
      <td class="p-3 border-b border-slate-800 font-semibold text-sm">🔒 Calidad Técnica</td>
      <td class="p-3 border-b border-slate-800 text-slate-400 text-xs">Robustez, confiabilidad y seguridad de la solución</td>
      <td class="p-3 border-b border-slate-800 text-center"><span class="bg-blue-500/20 text-blue-300 px-3 py-1 rounded-full font-black text-base border border-blue-500/30">4</span></td>
      <td class="p-3 border-b border-slate-800 text-center"><span class="bg-slate-500/20 text-slate-300 px-3 py-1 rounded-full font-black text-base border border-slate-500/30">3</span></td>
    </tr>
    <tr class="hover:bg-white/5 transition-colors v-click">
      <td class="p-3 border-b border-slate-800 font-semibold text-sm">💰 Ahorro en Costos Operacionales</td>
      <td class="p-3 border-b border-slate-800 text-slate-400 text-xs">¿Permite ahorrar dinero en el mediano/largo plazo?</td>
      <td class="p-3 border-b border-slate-800 text-center"><span class="bg-blue-500/20 text-blue-300 px-3 py-1 rounded-full font-black text-base border border-blue-500/30">4</span></td>
      <td class="p-3 border-b border-slate-800 text-center"><span class="bg-slate-500/20 text-slate-300 px-3 py-1 rounded-full font-black text-base border border-slate-500/30">2</span></td>
    </tr>
    <tr class="bg-slate-900/60 v-click">
      <td class="p-3 font-black text-white text-sm">Puntaje P (Total)</td>
      <td class="p-3 text-slate-500 text-xs italic">Suma simple de atributos</td>
      <td class="p-3 text-center font-black font-mono text-blue-400 text-2xl drop-shadow-[0_0_8px_rgba(96,165,250,0.8)]">18</td>
      <td class="p-3 text-center font-black font-mono text-cyan-400 text-2xl">11</td>
    </tr>
  </tbody>
</table>
</div>

<p class="mt-3 text-xs text-slate-500 text-center v-click">
  ⚠️ El puntaje P es solo un indicador cualitativo de eficiencia. La decisión final requiere también el análisis de costos (VAC/P).
</p>

---
layout: default
transition: cube-left
---

# Acto 6: Estructura de Costos y VAC

<p class="text-slate-400 text-[0.75rem] mb-2 flex justify-between">
  <span>Horizonte: <strong class="text-white">5 años</strong> · Tasa: <strong class="text-white">8% anual</strong> · Moneda: <strong class="text-white">CLP</strong></span>
  <span>FA(8%, 5 años) = <strong class="text-slate-300">3.9927</strong></span>
</p>

<div class="grid grid-cols-2 gap-3 v-click">

<div class="glass-panel p-3 border-l-4 border-blue-500 flex flex-col justify-between">
  <div>
    <h3 class="text-blue-400 font-bold text-sm mb-2">Alt. 1 — Desarrollo Propio</h3>
    <table class="w-full text-[0.7rem] text-slate-300 border-collapse">
      <thead><tr class="text-slate-500 border-b border-slate-700"><th class="text-left pb-1">Ítem de Costo</th><th class="text-right pb-1">Año 0</th><th class="text-right pb-1">Años 1-5</th></tr></thead>
      <tbody>
        <tr class="border-b border-slate-800/50"><td class="py-0.5">Desarrollo de software</td><td class="text-right py-0.5 text-white">$30.000.000</td><td class="text-right py-0.5 text-slate-500">—</td></tr>
        <tr class="border-b border-slate-800/50"><td class="py-0.5">Infraestructura (cloud)</td><td class="text-right py-0.5 text-white">$8.000.000</td><td class="text-right py-0.5 text-white">$4.500.000</td></tr>
        <tr class="border-b border-slate-800/50"><td class="py-0.5">Personal técnico</td><td class="text-right py-0.5 text-slate-500">—</td><td class="text-right py-0.5 text-white">$2.000.000</td></tr>
        <tr class="border-b border-slate-800/50"><td class="py-0.5">Capacitación</td><td class="text-right py-0.5 text-white">$2.000.000</td><td class="text-right py-0.5 text-slate-500">—</td></tr>
        <tr class="border-b border-slate-800/50"><td class="py-0.5">Licencias (open source)</td><td class="text-right py-0.5 text-slate-500">—</td><td class="text-right py-0.5 text-white">$0</td></tr>
        <tr class="font-bold text-white border-t border-slate-600"><td class="py-0.5">Subtotal</td><td class="text-right py-0.5">$40.000.000</td><td class="text-right py-0.5">$6.500.000</td></tr>
      </tbody>
    </table>
  </div>
  <div class="mt-2 p-1.5 bg-blue-900/30 rounded-lg border border-blue-500/30 text-center">
    <p class="text-slate-400 text-[0.65rem]">VAC = $40M + $6,5M × FA(8%,5)</p>
    <p class="text-blue-400 text-base font-black mt-0.5 leading-none">VAC = $65.971.370</p>
  </div>
</div>

<div class="glass-panel p-3 border-l-4 border-cyan-500 flex flex-col justify-between">
  <div>
    <h3 class="text-cyan-400 font-bold text-sm mb-2">Alt. 2 — Power Platform</h3>
    <table class="w-full text-[0.7rem] text-slate-300 border-collapse">
      <thead><tr class="text-slate-500 border-b border-slate-700"><th class="text-left pb-1">Ítem de Costo</th><th class="text-right pb-1">Año 0</th><th class="text-right pb-1">Años 1-5</th></tr></thead>
      <tbody>
        <tr class="border-b border-slate-800/50"><td class="py-0.5">Configuración e implement.</td><td class="text-right py-0.5 text-white">$8.000.000</td><td class="text-right py-0.5 text-slate-500">—</td></tr>
        <tr class="border-b border-slate-800/50"><td class="py-0.5">Licencias Power Platform</td><td class="text-right py-0.5 text-slate-500">—</td><td class="text-right py-0.5 text-white">$9.000.000</td></tr>
        <tr class="border-b border-slate-800/50"><td class="py-0.5">Azure Hosting</td><td class="text-right py-0.5 text-slate-500">—</td><td class="text-right py-0.5 text-white">$3.500.000</td></tr>
        <tr class="border-b border-slate-800/50"><td class="py-0.5">Soporte técnico Microsoft</td><td class="text-right py-0.5 text-slate-500">—</td><td class="text-right py-0.5 text-white">$2.000.000</td></tr>
        <tr class="border-b border-slate-800/50"><td class="py-0.5">Capacitación</td><td class="text-right py-0.5 text-white">$3.000.000</td><td class="text-right py-0.5 text-slate-500">—</td></tr>
        <tr class="font-bold text-white border-t border-slate-600"><td class="py-0.5">Subtotal</td><td class="text-right py-0.5">$11.000.000</td><td class="text-right py-0.5">$14.500.000</td></tr>
      </tbody>
    </table>
  </div>
  <div class="mt-2 p-1.5 bg-cyan-900/30 rounded-lg border border-cyan-500/30 text-center">
    <p class="text-slate-400 text-[0.65rem]">VAC = $11M + $14,5M × FA(8%,5)</p>
    <p class="text-cyan-400 text-base font-black mt-0.5 leading-none">VAC = $68.928.180</p>
  </div>
</div>

</div>

---
layout: default
transition: flip-y
---

# Acto 7: Cálculo VAC/P y Análisis Comparativo

<p class="text-slate-400 text-xs mb-3">VAC/P = Costo por punto de eficiencia → <span class="text-cyan-400 font-bold">Menor valor = mejor relación costo-eficiencia</span></p>

<div class="glass-panel overflow-hidden border border-slate-700/50 v-click">
<table class="w-full text-left border-collapse text-xs">
  <thead>
    <tr class="bg-slate-800/90 text-white">
      <th class="p-3 border-b border-slate-700 text-sm">Indicador</th>
      <th class="p-3 border-b border-slate-700 text-center text-blue-400 font-bold">Alt. 1 — Desarrollo Propio</th>
      <th class="p-3 border-b border-slate-700 text-center text-cyan-400 font-bold">Alt. 2 — Power Platform</th>
    </tr>
  </thead>
  <tbody class="text-slate-200">
    <tr class="hover:bg-white/5 transition-colors v-click">
      <td class="p-3 border-b border-slate-800 font-semibold">Puntaje P (eficiencia)</td>
      <td class="p-3 border-b border-slate-800 text-center font-black text-blue-400 text-xl">18 pts</td>
      <td class="p-3 border-b border-slate-800 text-center font-black text-cyan-400 text-xl">11 pts</td>
    </tr>
    <tr class="hover:bg-white/5 transition-colors v-click">
      <td class="p-3 border-b border-slate-800 font-semibold">VAC (Valor Actual de Costos)</td>
      <td class="p-3 border-b border-slate-800 text-center font-mono text-red-400 text-base">$65.971.370</td>
      <td class="p-3 border-b border-slate-800 text-center font-mono text-red-400 text-base">$68.928.180</td>
    </tr>
    <tr class="v-click bg-slate-900/50">
      <td class="p-3 font-black text-white text-sm">VAC / P <span class="text-xs text-slate-400 font-normal ml-1">(costo por punto)</span></td>
      <td class="p-3 text-center font-black font-mono text-blue-400 text-2xl drop-shadow-[0_0_10px_rgba(96,165,250,0.6)]">$3.665.076</td>
      <td class="p-3 text-center font-bold font-mono text-cyan-300 text-xl">$6.266.198</td>
    </tr>
    <tr class="v-click">
      <td class="p-3 font-semibold text-slate-400">Interpretación</td>
      <td class="p-3 text-center"><span class="bg-green-500/20 text-green-400 px-3 py-1 rounded-full font-bold text-xs border border-green-500/30">✓ Recomendada</span></td>
      <td class="p-3 text-center"><span class="bg-yellow-500/20 text-yellow-400 px-3 py-1 rounded-full font-bold text-xs border border-yellow-500/30">Menos eficiente</span></td>
    </tr>
  </tbody>
</table>
</div>

<div class="mt-3 glass-panel p-3 border border-blue-500/30 bg-blue-900/20 text-xs text-slate-300 v-click">
  <span class="text-blue-400 font-bold">Análisis:</span> Aunque ambas alternativas tienen VAC similares, la Alt. 1 entrega <strong class="text-white">18 puntos de eficiencia vs 11</strong> de la Alt. 2. Por cada punto de eficiencia, la Alt. 1 cuesta <strong class="text-blue-300">$3.665.076</strong> mientras la Alt. 2 cuesta <strong class="text-red-400">$6.266.198</strong> — un <strong class="text-white">71% más caro</strong> por unidad de valor.
</div>

---
layout: center
class: bg-gradient-to-br from-[#0b1120] via-slate-900 to-[#032a3f]
transition: zoom-3d
---

<div class="max-w-3xl mx-auto text-center" v-motion :initial="{ scale: 0.9, opacity: 0 }" :enter="{ scale: 1, opacity: 1, transition: { duration: 1000, ease: 'easeOut' } }">
  
<div class="inline-block px-4 py-0.5 mb-4 rounded-full border border-cyan-400/40 bg-cyan-500/20 text-cyan-300 font-bold text-xs tracking-[0.2em] uppercase shadow-[0_0_15px_rgba(6,182,212,0.5)]">
  Veredicto Final
</div>

<h1 class="text-5xl font-black text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-cyan-300 mb-4 drop-shadow-2xl">
  Alternativa 1
</h1>

<h2 class="text-2xl font-light text-slate-200 mb-6">
  Desarrollo Propio Cloud-Native
</h2>

<div class="glass-panel p-6 text-left grid grid-cols-2 gap-5 relative glow-box">
  <div class="col-span-2 text-sm text-slate-300 text-center border-b border-slate-700/50 pb-4 leading-normal">
    Pese a tener una inversión inicial mayor, la Alt. 1 ofrece <strong class="text-white">mayor eficiencia por peso invertido</strong>, sin dependencia de licencias externas y con plena capacidad de adaptación al sistema de salud público chileno.
  </div>
  
  <div class="flex flex-col items-center justify-center text-center p-4 transition-transform hover:-translate-y-1">
    <div class="p-3 bg-blue-500/10 rounded-full mb-3 border border-blue-500/20">
      <carbon-rocket class="text-4xl text-blue-400 drop-shadow-[0_0_10px_rgba(59,130,246,0.8)]" />
    </div>
    <h3 class="font-bold text-white text-base">VAC/P Superior</h3>
    <p class="text-xs text-slate-400 mt-2 leading-normal">$3.665.076 vs $6.266.198 — 71% más eficiente en costo por punto de valor entregado.</p>
  </div>
  
  <div class="flex flex-col items-center justify-center text-center p-4 transition-transform hover:-translate-y-1">
    <div class="p-3 bg-cyan-500/10 rounded-full mb-3 border border-cyan-500/20">
      <carbon-chart-line-smooth class="text-4xl text-cyan-400 drop-shadow-[0_0_10px_rgba(6,182,212,0.8)]" />
    </div>
    <h3 class="font-bold text-white text-base">Escalabilidad Ilimitada</h3>
    <p class="text-xs text-slate-400 mt-2 leading-normal">Arquitectura preparada para integrarse con MINSAL y escalar a nivel nacional sin costos adicionales.</p>
  </div>
</div>

<div class="mt-6 text-cyan-500/60 font-mono text-xs v-click tracking-widest">
  > _Deploying future of healthcare... 100%_
</div>

</div>

---
layout: default
transition: cube-left
---

# Conclusión Final

<div class="grid grid-cols-2 gap-5 mt-4">

<div class="glass-panel p-5 v-click">
  <h3 class="text-white text-base font-bold mb-4 flex items-center gap-2"><carbon-chart-bar class="text-cyan-400" /> Resumen del Análisis</h3>
  <ul class="space-y-3 text-slate-300 text-xs">
    <li class="flex gap-2"><carbon-checkmark class="text-green-400 mt-0.5 shrink-0"/><span>MediClick aborda un problema real y urgente de acceso a medicamentos en Chile.</span></li>
    <li class="flex gap-2"><carbon-checkmark class="text-green-400 mt-0.5 shrink-0"/><span>Se evaluaron 2 alternativas mediante atributos cualitativos de eficiencia (escala 1–5).</span></li>
    <li class="flex gap-2"><carbon-checkmark class="text-green-400 mt-0.5 shrink-0"/><span>La Alt. 1 obtuvo <strong class="text-blue-400">P = 18</strong> vs <strong class="text-cyan-400">P = 11</strong> de la Alt. 2.</span></li>
    <li class="flex gap-2"><carbon-checkmark class="text-green-400 mt-0.5 shrink-0"/><span>Con VAC similares (~$66M vs ~$69M), el indicador VAC/P da ventaja clara a la Alt. 1.</span></li>
  </ul>
</div>

<div class="glass-panel p-5 v-click border border-blue-500/30 bg-blue-900/10">
  <h3 class="text-blue-400 text-base font-bold mb-4 flex items-center gap-2"><carbon-flow /> Decisión Recomendada</h3>
  <div class="text-center mb-4">
    <p class="text-2xl font-black text-white">Alternativa 1</p>
    <p class="text-blue-400 text-sm font-semibold mt-1">Desarrollo Propio Cloud-Native</p>
  </div>
  <p class="text-slate-300 text-xs leading-normal">
    Representa la mejor relación costo-eficiencia (<span class="text-blue-400 font-bold">VAC/P = $3.665.076</span>), mayor efectividad tecnológica y sostenibilidad financiera a largo plazo. La mayor inversión inicial se justifica por la reducción en costos de licencias y el control total sobre la plataforma.
  </p>
</div>

</div>

<div class="mt-4 glass-panel p-3 border border-cyan-500/20 text-center v-click">
  <p class="text-slate-400 text-xs">
    💡 <span class="text-cyan-400 font-bold">Nota importante:</span> El puntaje P refleja eficiencia cualitativa — no siempre la alternativa con mayor P es la mejor. En este caso, el bajo VAC/P de la Alt. 1 confirma que es también la opción <strong class="text-white">más económicamente sostenible</strong>.
  </p>
</div>

---
layout: center
class: text-center
transition: fade
---

<h1 class="text-5xl font-black mb-8">Gracias</h1>

<div class="mt-8 flex justify-center">
  <img src="/logo_nuevo.png" class="h-28 object-contain drop-shadow-[0_0_20px_rgba(14,165,233,0.5)]" />
</div>

<div class="mt-10 flex justify-center gap-8 text-slate-400 text-base font-light">
  <span class="flex items-center gap-2 hover:text-cyan-400 transition-colors cursor-pointer"><carbon-logo-github /> /MediClick</span>
  <span class="flex items-center gap-2 hover:text-cyan-400 transition-colors cursor-pointer"><carbon-email /> hello@mediclick.app</span>
</div>
