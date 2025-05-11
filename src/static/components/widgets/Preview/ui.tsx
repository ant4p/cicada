import type {TPreview} from "./types.ts";
import type {FC} from "react"
import Contact from "@/components/shared/Contact";
import {Image} from "minista";
import "./Preview.scss"

const Preview: FC<TPreview> = () => {
  return (
    <section className="preview">
      <div className="preview__inner container">
        <h1 className="preview__title title title--big">От идеи до 3D печати — с нами это лекго реализовать</h1>
        <div className="preview__subtext text">
          Изготавливаем 3D-фигуры, игрушки, сувениры, детали или что‑то уникальное — мы готовы к любым задачам!
        </div>
         <Image
          className="preview__image"
          src="/src/assets/images/content/preview.jpg"
          alt="3D принтер"
        />
        <div className="preview__description text">
          <p className="preview__description-text">
            Создаём уникальные изделия, которые радуют и вдохновляют. Используем современные технологии SLA и FDM, а
            также материалы премиум-класса для достижения высокого качества и долговечности каждого проекта
          </p>
          <div className="preview__description-links">
            <Contact className="preview__description-link" type="telegram"/>
            <Contact className="preview__description-link" type="whatsapp" />
          </div>
         </div>


      </div>
    </section>
  )
}

export default Preview