import type {FC} from "react"
import SectionHeader from "@/components/shared/SectionHeader";
import "./Advantages.scss"

const Advantages: FC = () => {
  return (
    <section className="advantages">
      <div className="advantages__inner container">
        <SectionHeader title="Почему выбирают CICADA 3D мастерскую?" subtitle="преимущества работать с нами"/>
        <div className="advantages__body">
          <article className="advantages__advantage">
            <h3 className="advantages__advantage-title text text--big">Более 15 современных принтеров SLA и FDM</h3>
            <div className="advantages__advantage-text text text--regular">
              Чтобы создавать детали с высокой точностью,
              сложной геометрией и безупречной обработкой поверхности
            </div>
          </article>
          <article className="advantages__advantage">
            <h3 className="advantages__advantage-title text text--big">Работа с широким спектром материалов</h3>
            <div className="advantages__advantage-text text text--regular">
              Чтобы создавать детали с высокой точностью, сложной геометрией и безупречной обработкой поверхности
            </div>
          </article>
          <article className="advantages__advantage">
            <h3 className="advantages__advantage-title text text--big">От 3D-сканирования до постобработки</h3>
            <div className="advantages__advantage-text text text--regular">
              Чтобы создавать детали с высокой точностью, сложной геометрией и безупречной обработкой поверхности
            </div>
          </article>

          <article className="advantages__advantage">
            <h3 className="advantages__advantage-title text text--big">Производства без потери качества</h3>
            <div className="advantages__advantage-text text text--regular">
              Чтобы создавать детали с высокой точностью, сложной геометрией и безупречной обработкой поверхности
            </div>
          </article>
        </div>
      </div>
    </section>
  )
}

export default Advantages