import Preview from "@/components/widgets/Preview";
import Services from "@/components/widgets/Services";
import ReadyProjects from "@/components/widgets/ReadyProjects";
import Contacts from "@/components/widgets/Contacts";
import Address from "@/components/widgets/Address";
import Print from "@/components/widgets/Print";
import Projects from "../components/widgets/Projects";


export default function () {
  return (
    <>
      <Preview/>
      <Services/>
      <ReadyProjects/>
      <Print/>
      <Projects subtitle="3D Моделирование"/>
      <Projects subtitle="3D Сканирование"/>
      <Contacts/>
      <Address/>
    </>
  )
}
