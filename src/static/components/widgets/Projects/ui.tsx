import type {TProjects} from "./type";
import type {FC} from "react"
import SectionHeader from "@/components/shared/SectionHeader";
import {Image} from "minista";
import "./Projects.scss"

const Projects: FC<TProjects> = (props) => {
  const {
    subtitle,
    images = [
      {image: "content/product.jpg", link: "/"} ,
      {image: "content/product_2.jpg", link: "/"} ,
      {image: "content/product_2.jpg", link: "/"} ,
      {image: "content/product_2.jpg", link: "/"} ,
      {image: "content/product_2.jpg", link: "/"} ,
      {image: "content/product_2.jpg", link: "/"} ,
      {image: "content/product_2.jpg", link: "/"} ,
      {image: "content/product_2.jpg", link: "/"} ,
      {image: "content/product_2.jpg", link: "/"} ,
    ]
  } = props


  return (
    <section className="projects">
      <div className="projects__inner container">
        <SectionHeader title="Наши работы" subtitle={subtitle}/>
        <swiper-container class="projects__slider" slides-per-view="1.4" space-between="10" centered-slides="true">
          {images.map(({image, link}) => (
            <swiper-slide key={image}>
              <a href={link} className="projects__link">
                <Image
                  className="projects__image"
                  src={`/src/assets/images/${image}`}
                  alt="Продукт"
                />
              </a>
            </swiper-slide>
          ))}
        </swiper-container>
        <ul className="projects__list">
          {images.map(({image, link}) => (
            <li className="projects__item" key={image}>
              <a href={link} className="projects__link">
                <Image
                  className="projects__image"
                  src={`/src/assets/images/${image}`}
                  alt="Продукт"
                />
              </a>
            </li>
            ))}
        </ul>
      </div>

    </section>
)
}

export default Projects