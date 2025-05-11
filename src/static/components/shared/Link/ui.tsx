import type { FC } from "react"
import classNames from "classnames"
import { TLink } from "./types"
import "./Link.scss"

const Link: FC<TLink> = (props) => {
  const {
    className,
    children,
    href,
    ...rest
  } = props

  return (
    <a
      className={classNames(className, "link")}
      href={href}
      {...rest}
    >
      {children}
    </a>
  )
}

export default Link