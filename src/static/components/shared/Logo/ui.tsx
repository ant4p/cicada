import type {TLogo} from "./types.ts";
import type {FC} from "react"
import classNames from "classnames";
import {Image} from "minista";

const Logo: FC<TLogo> = (props) => {
  const {
    className,
  } = props

  return (
    <a className={classNames(className, "logo")} href="/" aria-label="go to home page">
      <Image
        className="logo__image"
        title="to home page"
        src="/src/assets/images/logo.png"
        alt="cicada logo"
      />
    </a>
  )
}

export default Logo