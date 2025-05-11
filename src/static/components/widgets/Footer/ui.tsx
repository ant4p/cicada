import type {FC} from "react"
import "./Footer.scss"
import Logo from "@/components/shared/Logo";
import Link from "@/components/shared/Link";

const Footer: FC = () => {
  return (
    <footer className="footer">
      <div className="footer__inner container">
        <div className="footer__body">
          <Logo className="footer__logo"/>
          <div className="footer__links">
            <Link className="footer__link" href="/">Статьи</Link>
            <Link className="footer__link" href="/">О нас</Link>
            <a className="footer__link footer__vk" href="/">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect width="24" height="24" rx="12" fill="#0077FF"/>
                <path
                  d="M12.5879 16.2C8.07801 16.2 5.50562 13.0469 5.39844 7.80005H7.65753C7.73173 11.6511 9.39719 13.2823 10.7164 13.6187V7.80005H12.8435V11.1214C14.1462 10.9784 15.5149 9.46491 15.9766 7.80005H18.1037C17.9298 8.6635 17.583 9.48104 17.085 10.2015C16.5871 10.9221 15.9487 11.53 15.2098 11.9874C16.0346 12.4054 16.763 12.9969 17.3471 13.7231C17.9313 14.4492 18.3577 15.2935 18.5984 16.2H16.2569C16.0408 15.4126 15.6017 14.7077 14.9945 14.1737C14.3873 13.6398 13.639 13.3004 12.8435 13.1982V16.2H12.5879Z"
                  fill="white"
                />
              </svg>
            </a>
          </div>
        </div>
        <small className="footer__copy text">CICADA © 2025</small>
      </div>
    </footer>
  )
}

export default Footer