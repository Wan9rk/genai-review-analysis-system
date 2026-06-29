export const DESIGN_W = 1920
export const DESIGN_H = 1080

let handler = null

export function initScreenAdapter(el) {
  function fit() {
    const ww = window.innerWidth
    const wh = window.innerHeight
    const scale = Math.min(ww / DESIGN_W, wh / DESIGN_H)

    el.style.position = 'absolute'
    el.style.width = DESIGN_W + 'px'
    el.style.height = DESIGN_H + 'px'
    el.style.left = ((ww - DESIGN_W * scale) / 2) + 'px'
    el.style.top = ((wh - DESIGN_H * scale) / 2) + 'px'
    el.style.transform = `scale(${scale})`
    el.style.transformOrigin = 'left top'
    el.style.margin = '0'
  }
  fit()
  handler = fit
  window.addEventListener('resize', fit)
}

export function destroyScreenAdapter() {
  if (handler) {
    window.removeEventListener('resize', handler)
    handler = null
  }
}
