import type {FC} from "react"
import Contact from "@/components/shared/Contact";
import {Image} from "minista";
import {TServiceProduct} from "./type";
import "./ServiceProduct.scss"

const ServiceProduct: FC<TServiceProduct> = (props) => {
  const {
    image = "/src/assets/images/content/3d_printer.jpg",
    text = "            FDM-технология 3Д-печати – это самая распространенная, простая и доступная технология аддитивного\n" +
      "            производства (3D печать PETG пластиком на заказ). Суть ее заключается в расплавлении пластиковой нити и ее\n" +
      "            нанесении слой за слоем в соответствии с запрограммированной моделью. Все слои имеют одинаковую толщину,\n" +
      "            определенную параметрами печати и нарезки модели. Нарезка модели осуществляется в специальной программе –\n" +
      "            слайсере. На основании нарезки формируется специальный G-CODE, который служит набором команд для принтера и\n" +
      "            3Д-печати.",
    price = "от 6₽/см³",
    title = "ABS PLA пластиком"
  } = props

  return (
    <article className="service-product">
      <div className="service-product__container">
        <Image
          className="service-product__image"
          src={image}
          alt="Продукт"
        />
      </div>
      <div className="service-product__body">
        <h3 className="service-product__title text text--big">{title}</h3>
        <div className="service-product__price text text--big">{price}</div>
        <div className="service-product__description text text--regular">
          <p>
            {text}
          </p>
        </div>
        <address className="service-product__contacts">
          <Contact className="service-product__contact is-small-mobile-small" type="whatsapp"/>
          <Contact className="service-product__contact is-small-mobile-small" type="telegram"/>
          <Contact className="service-product__contact is-mail" type="mail"/>
          <Contact className="service-product__contact is-phone" type="phone"/>
        </address>
      </div>
    </article>
  )
}

export default ServiceProduct