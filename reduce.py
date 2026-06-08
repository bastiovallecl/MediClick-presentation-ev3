import sys

with open('slides.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Acto 1
content = content.replace('<div class=""grid grid-cols-2 gap-6 mt-4"">', '<div class=""grid grid-cols-2 gap-5 mt-1"">')
content = content.replace('<div class=""glass-panel p-5 v-click""', '<div class=""glass-panel p-4 v-click""')
content = content.replace('<h3 class=""text-lg font-bold text-white mb-4 flex items-center gap-2"">', '<h3 class=""text-lg font-bold text-white mb-2 flex items-center gap-2"">')
content = content.replace('<ul class=""space-y-3 text-slate-300 text-sm"">', '<ul class=""space-y-2 text-slate-300 text-sm"">')

# Contexto
content = content.replace('<div class=""grid grid-cols-3 gap-4 mt-4"">', '<div class=""grid grid-cols-3 gap-3 mt-1"">')
content = content.replace('p-4 v-click border-l-4', 'p-3 v-click border-l-4')
content = content.replace('font-bold mb-3', 'font-bold mb-2')
content = content.replace('leading-relaxed', 'leading-normal')
content = content.replace('<ul class=""text-slate-300 text-xs space-y-1.5 leading-relaxed"">', '<ul class=""text-slate-300 text-xs space-y-1 leading-normal"">')
content = content.replace('<p class=""mt-4 text-center text-slate-500 text-xs v-click"">', '<p class=""mt-2 text-center text-slate-500 text-xs v-click"">')

# Flujo (Mermaid)
content = content.replace('<div class=""mt-4 glass-panel p-5 rounded-2xl v-click glow-box"">', '<div class=""mt-1 glass-panel p-3 rounded-2xl v-click glow-box scale-[0.85] origin-top"">')
content = content.replace('<p class=""text-center text-cyan-400 mt-3 v-click text-xs font-medium"">', '<p class=""text-center text-cyan-400 mt-0 v-click text-xs font-medium"">')

# Inteligencia Artificial
content = content.replace('<div class=""pr-6 mt-2"">', '<div class=""pr-6 mt-1"">')
content = content.replace('<div class=""space-y-4"">', '<div class=""space-y-2"">')

# Acto 4 Menu
content = content.replace('<h1 class=""text-5xl font-black text-white mb-10 drop-shadow-[0_0_20px_rgba(255,255,255,0.3)]"">', '<h1 class=""text-4xl font-black text-white mb-5 drop-shadow-[0_0_20px_rgba(255,255,255,0.3)]"">')
content = content.replace('<div class=""glass-panel p-8 relative overflow-hidden', '<div class=""glass-panel p-6 relative overflow-hidden')
content = content.replace('<div class=""glass-panel p-8 border border-slate-700', '<div class=""glass-panel p-6 border border-slate-700')

# Acto 4 Detalle 1 & 2
content = content.replace('<div class=""glass-panel p-6 relative overflow-hidden group w-full max-w-2xl glow-box"">', '<div class=""glass-panel p-4 relative overflow-hidden group w-full max-w-2xl glow-box"">')
content = content.replace('<h4 class=""text-blue-400 text-2xl font-black mb-5"">', '<h4 class=""text-blue-400 text-2xl font-black mb-3"">')
content = content.replace('<h4 class=""text-cyan-400 text-2xl font-black mb-5"">', '<h4 class=""text-cyan-400 text-2xl font-black mb-3"">')
content = content.replace('<div class=""flex gap-4 mb-5 justify-center"">', '<div class=""flex gap-4 mb-3 justify-center"">')
content = content.replace('<div class=""flex gap-5 mb-5 justify-center"">', '<div class=""flex gap-5 mb-3 justify-center"">')

# Acto 5 Evaluacion
content = content.replace('<p class=""text-slate-400 text-xs mb-3"">Escala 1', '<p class=""text-slate-400 text-xs mb-1"">Escala 1')
content = content.replace('<th class=""p-3 border-b', '<th class=""p-2 border-b')
content = content.replace('<td class=""p-3 border-b', '<td class=""p-1.5 border-b')
content = content.replace('<td class=""p-3 font-black', '<td class=""p-1.5 font-black')
content = content.replace('<td class=""p-3 text-slate-500', '<td class=""p-1.5 text-slate-500')
content = content.replace('<td class=""p-3 text-center', '<td class=""p-1.5 text-center')

# Acto 6 Costos
content = content.replace('<p class=""text-slate-400 text-xs mb-3"">Horizonte', '<p class=""text-slate-400 text-xs mb-1"">Horizonte')
content = content.replace('<div class=""grid grid-cols-2 gap-4 v-click"">', '<div class=""grid grid-cols-2 gap-3 v-click"">')
content = content.replace('<div class=""glass-panel p-4 border-l-4', '<div class=""glass-panel p-3 border-l-4')
content = content.replace('<h3 class=""text-blue-400 font-bold text-sm mb-3"">', '<h3 class=""text-blue-400 font-bold text-sm mb-1"">')
content = content.replace('<h3 class=""text-cyan-400 font-bold text-sm mb-3"">', '<h3 class=""text-cyan-400 font-bold text-sm mb-1"">')
content = content.replace('pb-1.5', 'pb-1')
content = content.replace('py-1.5', 'py-0.5')
content = content.replace('<div class=""mt-3 p-2 bg-blue-900', '<div class=""mt-1 p-2 bg-blue-900')
content = content.replace('<div class=""mt-3 p-2 bg-cyan-900', '<div class=""mt-1 p-2 bg-cyan-900')

# Acto 7 Comparativo
content = content.replace('<p class=""text-slate-400 text-xs mb-3"">VAC/P', '<p class=""text-slate-400 text-xs mb-1"">VAC/P')
content = content.replace('<div class=""mt-3 glass-panel p-3', '<div class=""mt-1 glass-panel p-2')

# Veredicto Final
content = content.replace('<div class=""inline-block px-4 py-1.5 mb-4', '<div class=""inline-block px-4 py-1 mb-2')
content = content.replace('<h1 class=""text-5xl font-black text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-cyan-300 mb-4 drop-shadow-2xl"">', '<h1 class=""text-4xl font-black text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-cyan-300 mb-2 drop-shadow-2xl"">')
content = content.replace('<h2 class=""text-2xl font-light text-slate-200 mb-6"">', '<h2 class=""text-xl font-light text-slate-200 mb-4"">')
content = content.replace('<div class=""glass-panel p-6 text-left', '<div class=""glass-panel p-4 text-left')
content = content.replace('<div class=""mt-6 text-cyan-500/60', '<div class=""mt-2 text-cyan-500/60')

# Conclusion
content = content.replace('<div class=""grid grid-cols-2 gap-5 mt-4"">', '<div class=""grid grid-cols-2 gap-4 mt-2"">')
content = content.replace('<div class=""glass-panel p-5 v-click', '<div class=""glass-panel p-4 v-click')
content = content.replace('<h3 class=""text-white text-base font-bold mb-4', '<h3 class=""text-white text-base font-bold mb-2')
content = content.replace('<h3 class=""text-blue-400 text-base font-bold mb-4', '<h3 class=""text-blue-400 text-base font-bold mb-2')
content = content.replace('<div class=""text-center mb-4"">', '<div class=""text-center mb-2"">')
content = content.replace('<div class=""mt-4 glass-panel p-3 border border-cyan-500/20 text-center v-click"">', '<div class=""mt-2 glass-panel p-2 border border-cyan-500/20 text-center v-click"">')

with open('slides.md', 'w', encoding='utf-8') as f:
    f.write(content)
