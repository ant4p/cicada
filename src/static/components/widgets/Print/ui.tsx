import type {FC} from "react"
import SectionHeader from "@/components/shared/SectionHeader";
import {Image} from "minista";
import "./Print.scss"

const Print: FC = () => {
  const imagesSlider = [
    {image: "content/product.jpg", link: "/"},
    {image: "content/product_2.jpg", link: "/"},
    {image: "content/product_2.jpg", link: "/"},
    {image: "content/product_2.jpg", link: "/"},
    {image: "content/product_2.jpg", link: "/"},
    {image: "content/product_2.jpg", link: "/"},
    {image: "content/product_2.jpg", link: "/"},
  ]

  return (
    <section className="print">
      <div className="print__inner container">
        <SectionHeader title="Наши работы" subtitle="3D Печать"/>
        <swiper-container class="print__slider" slides-per-view="1.4" space-between="10" centered-slides="true">
          {imagesSlider.map(({image, link}) => (
            <swiper-slide key={image}>
              <a href={link} className="print__link">
                <Image
                  className="print__image"
                  src={`/src/assets/images/${image}`}
                  alt="Продукт"
                />
              </a>
            </swiper-slide>
            ))}
        </swiper-container>
        <ul className="print__list">
          {imagesSlider.map(({image, link}) => (
            <li className="print__item" key={image}>
              <a href={link} className="print__link">
                <Image
                  className="print__image"
                  src={`/src/assets/images/${image}`}
                  alt="Продукт"
                />
              </a>
            </li>
            ))}
          <li className="print__item">
          <div className="print__description text">
              <p>
                Наши работы — это демонстрация возможностей современных 3D-технологий и нашей экспертизы. Просматривая
                проекты, вы можете вдохновиться, понять, как лучше реализовать вашу идею, выбрать подходящую технологию
                или материал
              </p>
              <p>
                Это помогает нам вместе найти оптимальное решение и достичь наилучшего результата для вашего проекта
              </p>
            </div>
          </li>
        </ul>
      </div>
    </section>
  )
}

export default Print