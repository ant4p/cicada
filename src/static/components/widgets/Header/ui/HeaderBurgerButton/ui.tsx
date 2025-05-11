import type {THeaderBurgerButton} from "./types.ts";
import type { FC } from "react"
import classNames from "classnames";
import "./HeaderBurgerButton.scss"

const HeaderBurgerButton: FC<THeaderBurgerButton> = (props) => {
  const {
    className,
  } = props

  return (
    <button
      className={classNames(className,
        'burger-button',
      )}
      data-burger-button
    >
      <div className="burger-button__center">
        <div></div>
      </div>
    </button>
  )
}

export default HeaderBurgerButton