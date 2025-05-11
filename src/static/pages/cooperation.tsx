import FullCycle from "@/components/widgets/FullCycle";
import Achievements from "@/components/widgets/Achievements";
import Advantages from "@/components/widgets/Advantages";
import OurCase from "@/components/widgets/OurCase";
import Services from "@/components/widgets/Services";
import Projects from "@/components/widgets/Projects";
import Contacts from "@/components/widgets/Contacts";
import Address from "@/components/widgets/Address";


export default function () {
  return (
    <>
      <FullCycle/>
      <Achievements/>
      <Advantages/>
      <OurCase/>
      <Services/>
      <Projects subtitle="3D Печать"/>
      <Contacts/>
      <Address/>
    </>
  )
}
