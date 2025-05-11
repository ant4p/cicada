class CatalogSlider {
    constructor() {
        this.rootElement = document.querySelector('.catalog__slider')
        if (!this.rootElement) return
        this.initSettings()
    }

    initSettings() {
        const swiperParams = {
            slidesPerView: 2.5,
            spaceBetween: 8,
            breakpoints: {
                470: {
                    slidesPerView: 3.2,
                },
            },
        };

        Object.assign(this.rootElement, swiperParams);

        this.rootElement.initialize();
    }
}

export default CatalogSlider;