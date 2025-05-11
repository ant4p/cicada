import type {FC} from "react"
import Link from "@/components/shared/Link";
import Product from "@/components/shared/Product";
import "./Catalog.scss"

const Catalog: FC = () => {
  return (
    <section className="catalog">
      <div className="catalog__inner container">
        <div className="catalog__header">
          <h1 className="catalog__title title">КАТАЛОГ</h1>
          <div className="catalog__text text hidden-mobile">Приобрести изделие можно через WhatsApp / Telegram</div>
        </div>
        <ul className="catalog__filters">
          <li className="catalog__filter"><Link className="catalog__link" href="/catalog#toys">Игрушки</Link></li>
            <li className="catalog__filter"><Link className="catalog__link" href="/catalog#statuete">Статуэтки</Link></li>
            <li className="catalog__filter"><Link className="catalog__link" href="/catalog#puzzles">Головоломки</Link></li>
            <li className="catalog__filter"><Link className="catalog__link" href="/catalog#household">В хозяйстве пригодится</Link></li>
          </ul>
          <div className="catalog__body">
            <div className="catalog__products">
              <h2 className="catalog__label title title--small">ИГРУШКИ</h2>
              <div className="catalog__products-body">
                <Product
                  className="catalog__product"
                  link="/catalog/product" image="/src/assets/images/content/product.jpg"
                  price="1200" title="Подвижный Аксолотль"
                />
                <Product
                  className="catalog__product"
                  link="/catalog/product" image="/src/assets/images/content/product.jpg"
                  price="1200" title="Подвижный Аксолотль"
                />
                <Product
                  className="catalog__product"
                  link="/catalog/product" image="/src/assets/images/content/product.jpg"
                  price="1200" title="Подвижный Аксолотль"
                />
                <Product
                  className="catalog__product"
                  link="/catalog/product" image="/src/assets/images/content/product.jpg"
                  price="1200" title="Подвижный Аксолотль"
                />
                <Product
                  className="catalog__product"
                  link="/catalog/product" image="/src/assets/images/content/product.jpg"
                  price="1200" title="Подвижный Аксолотль"
                />
                <Product
                  className="catalog__product"
                  link="/catalog/product" image="/src/assets/images/content/product.jpg"
                  price="1200" title="Подвижный Аксолотль"
                />
                <Product
                  className="catalog__product"
                  link="/catalog/product" image="/src/assets/images/content/product.jpg"
                  price="1200" title="Подвижный Аксолотль"
                />
                <Product
                  className="catalog__product"
                  link="/catalog/product" image="/src/assets/images/content/product.jpg"
                  price="1200" title="Подвижный Аксолотль"
                />
              </div>
            </div>
            <div className="catalog__products" id="puzzles">
              <h2 className="catalog__label title title--small">Головоломки</h2>
              <div className="catalog__products-body">
                <Product
                  className="catalog__product"
                  link="/catalog/product" image="/src/assets/images/content/product.jpg"
                  price="1200" title="Подвижный Аксолотль"
                />
                <Product
                  className="catalog__product"
                  link="/catalog/product" image="/src/assets/images/content/product.jpg"
                  price="1200" title="Подвижный Аксолотль"
                />
                <Product
                  className="catalog__product"
                  link="/catalog/product" image="/src/assets/images/content/product.jpg"
                  price="1200" title="Подвижный Аксолотль"
                />

              </div>
            </div>
          </div>
      </div>
    </section>
)
}

export default Catalog