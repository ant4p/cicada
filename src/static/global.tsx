import {GlobalProps, Head} from "minista";
import Header from "@/static/components/widgets/Header";
import Footer from "@/static/components/widgets/Footer";
import "@/static/assets/styles"

export default function ({url, title, children}: GlobalProps) {
  return (
    <>
      <Head htmlAttributes={{lang: "ru"}}>
        <title></title>
        <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-element-bundle.min.js" defer />
        <script src="/d3/static/main.js" type="module"/>
      </Head>
      <Header/>
      <main className="main">
        {children}
      </main>
      <Footer/>
    </>
  )
}