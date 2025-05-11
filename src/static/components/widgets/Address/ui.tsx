import type { FC } from "react"
import {Image} from "minista";
import "./Address.scss"

const Address: FC = () => {
  return (
    <section className="address">
      <div className="address__inner container">
        <h2 className="address__title text text--main-2-light">Адрес</h2>
        <div className="address__address text text--big">улица Зои и Александра Космодемьянских, 26/21с1</div>
        <Image
          className="address__image"
          src="/src/assets/images/content/map.jpg"
          alt="Местоположение компании"
        />
      </div>
    </section>
  )
}

export default Address