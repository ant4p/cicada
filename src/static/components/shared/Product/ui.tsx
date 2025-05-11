import type {TProduct} from "./types.ts";
import type {FC} from "react"
import classNames from "classnames";
import {Image} from "minista";
import Contact from "@/components/shared/Contact";
import "./Product.scss"

const Product: FC<TProduct> = (props) => {
  const {
    className,
    link,
    image,
    title, price
  } = props

  return (
    <article className={classNames(className, "product")}>
      <a href={link} className="product__link" />
        <div className="product__preview">
          <div className="product__contacts">
            <Contact className="product__contact is-small-constant" type="telegram"/>
            <Contact className="product__contact is-small-constant" type="whatsapp"/>
          </div>
          <Image
            className="product__image"
            src={image}
            alt="Продукт"
          />
        </div>
        <div className="product__footer">
          <h3 className="product__title text text--regular">{title}</h3>
          <div className="product__price text text--regular">{price} ₽</div>
        </div>
    </article>
  )
}

export default Product