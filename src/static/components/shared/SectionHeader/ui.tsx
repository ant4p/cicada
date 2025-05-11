import {TSectionHeader} from "./types";
import type {FC} from "react"
import "./SectionHeader.scss"

const SectionHeader: FC<TSectionHeader> = (props) => {
  const {
    title,
    subtitle
  } = props

  return (
    <div className="section-header">
      <h2 className="section-header__title text text--main-2-light">{title}</h2>
      <div className="section-header__subtitle title">{subtitle}</div>
    </div>
  )
}

export default SectionHeader