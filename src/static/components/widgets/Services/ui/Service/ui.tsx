import type {TService} from "./types.ts";
import type {FC} from "react"
import classNames from "classnames";
import "./Service.scss"

const Service: FC<TService> = (props) => {
  const {
    title,
    text,
    className, link = "/"
  } = props

  return (
    <article className={classNames(className, "service")}>
      <a className="service__link" href={link}>
        <h3 className="service__title text text--big">{title}</h3>
        <p className="service__description text text--regular">{text}</p>
      </a>
    </article>
  )
}

export default Service