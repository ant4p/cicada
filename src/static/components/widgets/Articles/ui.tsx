import type { FC } from "react"
import Article from "./ui/Article";
import "./Articles.scss"

const Articles: FC = () => {
  return (
    <section className="articles">
      <div className="articles__inner container">
        <h1 className="articles__title title">Статьи</h1>
        <div className="articles__body">
          <Article/>
          <Article/>
          <Article/>
          <Article/>
          <Article/>
          <Article/>
        </div>
        <div className="articles__pagination">
          <button className="articles__pagination-button button is-arrow" type="button">
            <svg width="8" height="14" viewBox="0 0 8 14" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M7 13L1 7L7 1" stroke="white" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
            </svg>
          </button>
          <button className="articles__pagination-button is-active text" type="button">1</button>
          <button className="articles__pagination-button text" type="button">2</button>
          <button className="articles__pagination-button text" type="button">3</button>
          <button className="articles__pagination-button text" type="button">4</button>
          <button className="articles__pagination-button text" type="button">...</button>
          <button className="articles__pagination-button text" type="button">10</button>
          <button className="articles__pagination-button is-arrow" type="button">
            <svg width="8" height="14" viewBox="0 0 8 14" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M1 1L7 7L1 13" stroke="white" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
            </svg>
          </button>
        </div>
      </div>
    </section>
  )
}

export default Articles