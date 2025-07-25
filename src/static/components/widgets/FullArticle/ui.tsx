import type {FC} from "react"
import {Image} from "minista";
import "./FullArticle.scss"

const FullArticle: FC = () => {
  return (
    <section className="full-article">
      <div className="full-article container">
        <h1 className="full-article__title title">Как 3D-принтеры меняют индустрию</h1>
        <div className="full-article__body">
          <Image
            className="full-article__image"
            src="/src/assets/images/content/article.jpg"
            alt="Статья"
            width="1260" height="500" loading="lazy"
          />
          <div className="full-article__content">
            <div className="full-article__description text text--regular">
              <p>
                В последние годы 3D-принтеры стремительно проникают в различные сферы промышленности, предлагая
                принципиально новый подход к созданию изделий. Традиционные методы производства, такие как литьё под
                давлением, фрезеровка и штамповка, начинают уступать место аддитивным технологиям, которые позволяют
                создавать сложные геометрические формы с высокой точностью и минимальными затратами времени и ресурсов.
                Одним из ключевых преимуществ 3D-печати является возможность производить уникальные изделия малыми
                партиями без необходимости изготовления дорогостоящих форм и пресс-форм.
              </p>
              <p>
                Это особенно важно для отраслей, где требуется высокая степень кастомизации, таких как медицина,
                автомобилестроение и авиация. Например, в медицинской сфере 3D-принтеры используются для создания
                индивидуальных имплантатов, ортопедических устройств и даже органов для трансплантации.
              </p>
              <p>
                Кроме того, 3D-печать позволяет значительно сократить сроки разработки новых продуктов. Вместо долгих
                месяцев на создание прототипов и тестирование, инженеры могут быстро напечатать несколько вариантов
                изделия, внести необходимые изменения и сразу же перейти к производству финальной версии. Это ускоряет
                инновационный цикл и помогает компаниям быстрее выводить свои продукты на рынок.
              </p>
              <p>
                Ещё одним важным аспектом является снижение затрат на материалы. Аддитивные технологии позволяют
                минимизировать количество отходов, так как материал используется только там, где он необходим. Это
                делает
                производство более экономичным и экологически чистым.
              </p>
              <p>
                Однако, несмотря на все эти преимущества, внедрение 3D-печати сталкивается с рядом вызовов. Одним из них
                является необходимость адаптации существующих производственных процессов и обучения персонала новым
                технологиям. Также существуют ограничения по материалам, которые можно использовать для 3D-печати, хотя
                этот список постоянно расширяется.
              </p>
              <p>
                Тем не менее, будущее производства выглядит весьма многообещающим. С развитием технологий 3D-печати мы
                можем ожидать ещё большего проникновения этих методов в самые разные отрасли, что приведёт к дальнейшему
                росту эффективности и снижению себестоимости продукции.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}

export default FullArticle