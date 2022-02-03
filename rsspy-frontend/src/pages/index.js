import * as React from "react"
import Layout from "../components/layout"
import Seo from "../components/seo"
import { getLineChartData } from "../hooks/getLineChartData.js"
import { Line } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

const IndexPage = ({ serverData }) => {

  return (
    <Layout>
      <Seo title="Home" />
      <div style={{ width: '750px' }}>
        <Line data={serverData} />
      </div>
    </Layout>
  )
}

export default IndexPage

export async function getServerData() {

  try {

    const lineChartData = await getLineChartData()

    console.log(lineChartData)

    return {
      props: lineChartData,
    }

  } catch (error) {
    console.log(error)
    return {
      status: 500,
      headers: {},
      props: {}
    }
  }
}