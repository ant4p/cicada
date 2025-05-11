import type {FC} from "react"
import SectionHeader from "@/components/shared/SectionHeader";
import {Image} from "minista";
import "./OurCase.scss"

const OurCase: FC = () => {
  return (
    <section className="our-case">
      <div className="our-case__inner container">
        <SectionHeader title="Хотите увидеть ваш проект в наших кейсах?" subtitle="Наши кейсы"/>
        <div className="our-case__body">
          <Image
            className="our-case__image"
            src="/src/assets/images/content/case.jpg"
            alt="Case"
          />
          <div className="our-case__content">
            <h3 className="our-case__title title title--small">Кейс: Создание детских игрушек</h3>
            <div className="our-case__block">
              <div className="our-case__block-title  text text--big">Задача клиента:</div>
              <div className="our-case__block-text text">
                Создать линейку безопасных и ярких игрушек
                (корабликов, драконов) для продажи в детских магазинах. Основное требование — экологичность материалов
                и
                прочность изделий
              </div>
            </div>
            <div className="our-case__block">
              <div className="our-case__block-title text text--big">Решение от мастерской 3D CICADA</div>
              <div className="our-case__block-text text">
                Подготовка 3D-моделей для игрушек на основе эскизов клиента.<br/>
                • Печать изделий на FDM-принтерах с использованием PLA-пластика, безопасного для детей.<br/>
                • Детальная постобработка: шлифовка, окрашивание гипоаллергенными красками.
              </div>
            </div>
            <div className="our-case__block is-result">
              <div className="our-case__block-title text text--big">Результат:</div>
              <div className="our-case__block-text text">
                Завершение проекта за 14 рабочих дней. <br/>
                • Выпущено 100 изделий с высоким качеством детализации
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}

export default OurCase