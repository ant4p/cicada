class ProductSlider {
    constructor() {
        this.rootSlider = document.querySelector('.full-product__slider')
        this.thumbSlider = document.querySelector('.full-product__thumbs')

        if (!this.rootSlider || !this.thumbSlider) return
        this.initSettings()
    }

    initSettings() {
        const swiperParams = {
            spaceBetween: 20,
            navigation: {
                nextEl: '.full-product__navigation-button--next',
                prevEl: '.full-product__navigation-button--prev',
            },
            thumbs: {swiper: ".full-product__thumbs"},
        };

        const swiperThumbsParams = {
            slidesPerView: 4.8,
            spaceBetween: 10,
            breakpoints: {
                480: {
                    slidesPerView: 4.2,
                },
                640: {
                    slidesPerView: 3.5,
                },
                920: {
                    slidesPerView: 4.5,
                },
                1280: {
                    slidesPerView: 6,
                },
            },
        };

        Object.assign(this.thumbSlider, swiperThumbsParams);

        this.thumbSlider.initialize();

        Object.assign(this.rootSlider, swiperParams);

        this.rootSlider.initialize();


    }
}

export default ProductSlider;