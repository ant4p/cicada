import {FC} from "react"
import Logo from "@/components/shared/Logo";
import Link from "@/components/shared/Link";
import HeaderBurgerButton from "@/components/widgets/Header/ui/HeaderBurgerButton";
import Contact from "@/components/shared/Contact";
import "./Header.scss"

const Header: FC = () => {
  return (
    <header className="header">
      <div className="header__inner container">
        <Logo className="header__logo"/>
        <nav className="header__menu">
          <ul className="header__menu-list">
            <li className="header__menu-item"><Link href="/service">Услуги</Link></li>
            <li className="header__menu-item"><Link href="/catalog">Каталог</Link></li>
            <li className="header__menu-item"><Link href="/articles">Портфолио</Link></li>
            <li className="header__menu-item"><Link href="/">Контакты</Link></li>
            <li className="header__menu-item"><Link href="/cooperation">Сотрудничество</Link></li>
            <li className="header__menu-item visible-mobile"><HeaderBurgerButton className="header__burger-button"/></li>
          </ul>
        </nav>
      </div>
      <nav className="header__burger-menu visible-mobile" data-overlay-menu>
        <ul className="header__burger-menu-list">
          <li className="header__burger-menu-item"><Link href="/">Услуги</Link></li>
          <li className="header__burger-menu-item"><Link href="/">Каталог</Link></li>
          <li className="header__burger-menu-item"><Link href="/">Портфолио</Link></li>
          <li className="header__burger-menu-item"><Link href="/">Контакты</Link></li>
          <li className="header__burger-menu-item"><Link href="/">Сотрудничество</Link></li>
        </ul>
        <div className="header__burger-menu-links">
          <Contact className="header__burger-menu-link is-mobile" type="telegram" />
          <Contact className="header__burger-menu-link is-mobile" type="whatsapp" />
          <Contact className="header__burger-menu-link is-mail" type="mail"/>
          <Contact className="header__burger-menu-link is-phone" type="phone"/>
        </div>
      </nav>
    </header>
  )
}

export default Header