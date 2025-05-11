import type { FC } from "react"
import ServiceProduct from "./ui/ServiceProduct";
import "./ServiceProducts.scss"

const ServiceProducts: FC = () => {
  return (
    <section className="service-products">
      <div className="service-products__inner container">
        <h1 className="service-products__title title">3D печать</h1>
        <div className="service-products__body">
          <ServiceProduct/>
          <ServiceProduct/>
          <ServiceProduct/>
        </div>
      </div>
    </section>
  )
}

export default ServiceProducts