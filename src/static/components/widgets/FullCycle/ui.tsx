import type {FC} from "react"
import Contact from "@/components/shared/Contact";
import {Image} from "minista";
import "./FullCycle.scss"

const FullCycle: FC = () => {
  return (
    <section className="full-cycle">
      <div className="full-cycle__inner container">
        <div className="full-cycle__body">
          <Image
            className="full-cycle__image"
            src="/src/assets/images/content/full_cycle.jpg"
            alt="Наши продукты"
          />
          <h1 className="full-cycle__title title">полный цикл 3D производства для вашего бизнеса</h1>
          <div className="full-cycle__footer">
            <div className="full-cycle__description text">
              Сканирование, печать, моделирование, роспись и постобработка.
              Более 15 принтеров, современные технологии SLA и FDM, работа с любыми материалами
            </div>
            <div className="full-cycle__contacts">
              <Contact className="full-cycle__contact is-small-mobile-small" type="telegram"/>
              <Contact className="full-cycle__contact" type="whatsapp"/>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}

export default FullCycle