import type {TArticle} from "./types.ts";
import type {FC} from "react"
import {Image} from "minista";
import "./Article.scss"

const Article: FC<TArticle> = (props) => {
  const {
    link = "/articles/article",
    image = "/src/assets/images/content/article.jpg",
    title = "Как 3D-принтеры меняют индустрию",
    description = "В статье рассматривается влияние 3D-технологий на традиционные методы производства, приводятся примеры\n" +
      "          успешных кейсов внедрения аддитивных технологий в различных отраслях"
  } = props

  return (
    <article className="article">
      <a className="article__link" href={link}>
        <h3 className="article__title text text--big">{title}</h3>
        <Image
          className="article__image"
          src={image}
          alt="Статья"
        />
        <div className="article__description text text--regular">
          {description}
        </div>
      </a>
    </article>
  )
}

export default Article