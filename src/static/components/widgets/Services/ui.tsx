import type {FC} from "react"
import Service from "@/components/widgets/Services/ui/Service";
import Contact from "@/components/shared/Contact";
import SectionHeader from "@/components/shared/SectionHeader";
import "./Services.scss"

const Services: FC = () => {
  return (
    <section className="services">
      <div className="services__inner container">
        <SectionHeader title="Услуги" subtitle="Создаём качественные и уникальные проекты на заказ"/>
        <div className="services__body">
          <Service
            className="sevices__service"
            title="3D Печать"
            text="Мы используем современные 3D-принтеры для создания точных и качественных изделий. Игрушки, детали, макеты или сувениры — всё, что вы хотите, мы напечатаем из различных материалов, подбирая их под ваши потребности."
          />
          <Service
            className="sevices__service"
            title="3D Моделирование"
            text="Наши специалисты создадут уникальную 3D-модель с нуля или доработают вашу идею. Мы учитываем все пожелания, чтобы получить точный результат, который станет основой для печати или других проектов."
          />
          <Service
            className="sevices__service"
            title="3D Визуализация"
            text="Мы создаём фотореалистичные изображения ваших будущих изделий. Вы сможете увидеть, как будет выглядеть проект до его изготовления, и внести правки на этапе планирования."
          />
          <Service
            className="sevices__service"
            title="Роспись"
            text="Добавьте индивидуальности вашему изделию с помощью профессиональной росписи. Мы используем стойкие краски и художественный подход, чтобы создать яркий и уникальный дизайн."
          />
          <Service
            className="sevices__service"
            title="Постобработка"
            text="После печати мы доводим изделия до совершенства: удаляем лишний материал, шлифуем поверхности, окрашиваем и собираем конструкцию, чтобы готовый продукт выглядел идеально."
          />
          <div className="services__contact">
            <div className="services__contact-text text text--regular">
              Мы готовы помочь реализовать любые ваши идеи с использованием
              современных технологий и материалов
            </div>
            <div className="services__contact-body">
              <Contact className="services__contact-item" type="telegram"/>
              <Contact className="services__contact-item" type="whatsapp"/>
            </div>
          </div>
        </div>
      </div>

    </section>
  )
}

export default Services