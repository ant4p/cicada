class BurgerButton {
    selectors = {
        root: '[data-burger-button]',
    }

    stateClasses = {
        isActive: 'is-active'
    }

    state = {
        isActive: false
    }

    constructor() {
        this.rootElement = document.querySelector(this.selectors.root)
        if (!this.rootElement) return

        this.bindEvenets()
    }

    open() {
        this.rootElement.classList.add(this.stateClasses.isActive)
        this.state.isActive = true
        App.OverlayMenu.open()

    }
    close() {
        this.rootElement.classList.remove(this.stateClasses.isActive)
        this.state.isActive = false
        App.OverlayMenu.close()

    }
    toggle() {
        this.rootElement.classList.toggle(this.stateClasses.isActive)
        this.state.isActive = !this.state.isActive
        App.OverlayMenu.toggle()

    }
    onCLick() {

        this.toggle()
    }


    bindEvenets() {
        this.rootElement.addEventListener('click', () => this.onCLick())
    }
}

export default BurgerButton