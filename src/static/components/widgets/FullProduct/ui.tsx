import type {FC} from "react"
import type {TFullProduct} from "./type";
import Contact from "@/components/shared/Contact";
import Product from "@/components/shared/Product";
import {Image} from "minista";
import "./FullProduct.scss"

const FullProduct: FC<TFullProduct> = (props) => {
  const {
    title,
    images,
    description,
  } = props


  return (
    <section className="full-product">
      <div className="full-product__inner container">
        <h1 className="full-product__title title">{title}</h1>
        <div className="full-product__body">
          <div className="full-product__preview">
            <div className="full-product__slider-container">
              <swiper-container class="full-product__slider" init="false">
                {images.map((image) => (
                  <swiper-slide key={image}>
                    <Image
                      className="full-product__image"
                      src={`/src/assets/images/${image}`}
                      alt="Продукт"
                    />
                  </swiper-slide>
                ))}
              </swiper-container>
              <button className="full-product__navigation-button full-product__navigation-button--prev">
                <svg width="8" height="14" viewBox="0 0 8 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M7 13L1 7L7 1" stroke="white" strokeWidth="2" strokeLinecap="round"
                        strokeLinejoin="round"/>
                </svg>
              </button>
              <button className="full-product__navigation-button full-product__navigation-button--next">
                <svg width="8" height="14" viewBox="0 0 8 14" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M1 1L7 7L1 13" stroke="white" strokeWidth="2" strokeLinecap="round"
                        strokeLinejoin="round"/>
                </svg>
              </button>
            </div>
            <swiper-container class="full-product__thumbs" init="false">
              {images.map((image) => (
                <swiper-slide key={image}>
                  <Image
                    className="full-product__image is-thumb"
                    src={`/src/assets/images/${image}`}
                    alt="Продукт"
                  />
                </swiper-slide>
              ))}
            </swiper-container>
          </div>
          <div className="full-product__content">
            <div className="full-product__price text text--very-big">1200 ₽</div>
            <div className="full-product__contacts">
              <Contact className="full-product__contact" type="telegram"/>
              <Contact className="full-product__contact" type="whatsapp"/>
            </div>
            <div className="full-product__block is-description">
              <div className="full-product__block-label text text--main-2-light">Описание:</div>
              <div className="full-product__block full-product__description text">
                {description}
              </div>
            </div>
            <div className="full-product__block">
              <div className="full-product__block-label text text--main-2-light">Оплата и доставка</div>
              <div className="full-product__block-text text">
                <p>
                  Мы работаем с надёжной службой доставки CDEK, чтобы ваш заказ прибыл быстро и в целости. Либо вы
                  можете забрать товар из нашей мастерской. Оплата осуществляется удобным переводом на карту после
                  согласования всех деталей. Оформляйте заказ, и мы позаботимся о всём остальном!
                </p>
              </div>
            </div>
          </div>
        </div>
        <div className="full-product__footer">
          <h2 className="full-product__footer-title title">Смотрите также</h2>
          <div className="full-product__footer-body">
            <Product
              className="full-product__footer-product"
              link="/catalog/product" image="/src/assets/images/content/product.jpg"
              price="1200" title="Подвижный Аксолотль"
            />
            <Product
              className="full-product__footer-product"
              link="/catalog/product" image="/src/assets/images/content/product.jpg"
              price="1200" title="Подвижный Аксолотль"
            />
            <Product
              className="full-product__footer-product"
              link="/catalog/product" image="/src/assets/images/content/product.jpg"
              price="1200" title="Подвижный Аксолотль"
            />
            <Product
              className="full-product__footer-product"
              link="/catalog/product" image="/src/assets/images/content/product.jpg"
              price="1200" title="Подвижный Аксолотль"
            />
          </div>
        </div>
      </div>
    </section>
  )
}

export default FullProduct