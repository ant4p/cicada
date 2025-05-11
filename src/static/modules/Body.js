class Body {
    stateClasses = {
        isMuted: 'is-muted',
    }

    state = {
        isMuted : false
    }
    constructor() {
        this.rootElement = document.body
    }

    add() {
        this.rootElement.classList.add(this.stateClasses.isMuted)
        this.state.isMuted = true
    }

    remove() {
        this.rootElement.classList.remove(this.stateClasses.isMuted)
        this.state.isMuted = false

    }

    toggle() {
        this.rootElement.classList.toggle(this.stateClasses.isMuted)
        this.state.isMuted = !this.state.isMuted

    }
}

export default Body