import * as React from "react"
import Layout from "../components/layout"
import Seo from "../components/seo"
import {LineChart} from "../components/LineChart"

const IndexPage = () => (
  
  <Layout>
    <Seo title="Home" />
    <LineChart></LineChart>
  </Layout>
)

export default IndexPage
