import type {FC} from "react"
import SectionHeader from "@/components/shared/SectionHeader";
import "./Contacts.scss"

const Contacts: FC = () => {
  return (
    <section className="contacts">
      <div className="contacts__inner container">
        <SectionHeader title="Мы всегда на связи" subtitle="Контакты"/>
        <div className="contacts__text text">
          Расскажите нам о своём проекте, и мы поможем воплотить его в реальность.
          Игрушки, сувениры, детали или что‑то уникальное — мы готовы к любым задачам!
        </div>
        <address className="contacts__body">
          <a className="contacts__contact text text--big is-phone" href="tel:+7 (XXX) XXX-XX-XX"> +7 (XXX) XXX-XX-XX</a>
          <a className="contacts__contact text text--big is-mail" href="mailto:info@cicada3d.ru"> info@cicada3d.ru</a>
          <a className="contacts__contact is-whatsapp text text--big" href="/"> WhatsApp</a>
          <a className="contacts__contact is-telegram text text--big" href="/"> Telegram</a>
        </address>
      </div>
    </section>
  )
}

export default Contacts