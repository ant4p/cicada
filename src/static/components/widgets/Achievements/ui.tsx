import type {FC} from "react"
import SectionHeader from "@/components/shared/SectionHeader";
import "./Achievements.scss"

const Achievements: FC = () => {
  return (
    <section className="achievements">
      <div className="achievements__inner container">
        <SectionHeader title="Воплощаем идеи в реальность" subtitle="Наши достижения в цифрах"/>
        <div className="achievements__body">
          <article className="achievements__achievement">
            <div className="achievements__achievement-number">150</div>
            <div className="achievements__achievement-text text text--regular">Выполненных проектов</div>
          </article>
          <article className="achievements__achievement">
            <div className="achievements__achievement-number">15</div>
            <div className="achievements__achievement-text text text--regular">
              Дней средний срок реализации проекта
            </div>
          </article>
          <article className="achievements__achievement">
            <div className="achievements__achievement-number">95%</div>
            <div className="achievements__achievement-text text text--regular">
              Клиентов возвращаются с новыми задачами
            </div>
          </article>
        </div>
      </div>
    </section>
  )
}

export default Achievements