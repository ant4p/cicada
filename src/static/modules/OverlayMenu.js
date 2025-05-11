class OverlayMenu {
    selectors = {
        root: '[data-overlay-menu]',
    }

    stateClasses = {
        isActive: 'is-active',

    }

    state = {
        isActive: false
    }
    constructor() {
        this.rootElement = document.querySelector(this.selectors.root)
        if (!this.rootElement) return

        this.body = document.body
    }

    open() {
        this.rootElement.classList.add(this.stateClasses.isActive)
        App.Body.add()
        this.state.isActive = true
    }
    close() {
        this.rootElement.classList.remove(this.stateClasses.isActive)
        App.Body.remove()
        this.state.isActive = false
    }
    toggle() {
        console.log("aaaa")

        this.rootElement.classList.toggle(this.stateClasses.isActive)
        App.Body.toggle()
        this.state.isActive = !this.state.isActive
    }

}

export default OverlayMenu