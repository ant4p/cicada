import type {FC} from "react"
import SectionHeader from "@/components/shared/SectionHeader";
import Product from "@/components/shared/Product";
import Link from "@/components/shared/Link";
import "./ReadyProjects.scss"

const ReadyProjects: FC = () => {
  return (
    <section className="ready-projects">
      <div className="ready-projects__inner container">
        <SectionHeader title="Готовые проекты" subtitle="Каталог"/>
        <div className="ready-projects__body">
          <Product
            className="ready-projects__product"
            link="/catalog/product" image="/src/assets/images/content/product.jpg"
            price="1200" title="Подвижный Аксолотль"
          />
          <Product
            className="ready-projects__product"
            link="/catalog/product" image="/src/assets/images/content/product.jpg"
            price="1200" title="Подвижный Аксолотль"
          />
          <div className="ready-projects__description">
            <div className="ready-projects__text text">
              Каждое из них напечатано из безопасных и прочных материалов, чтобы
              радовать вас или стать идеальным подарком для любимого человека
            </div>
            <Link className="ready-projects__catalog is-big" href="/">В каталог</Link>
          </div>
        </div>
      </div>
    </section>
  )
}

export default ReadyProjects