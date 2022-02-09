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
      <br/>
      <div>
        <h3>Alpha Build 0.1</h3>
        <ul style={{ listStyle: 'circle'}}>
        <li>Displays top 10 coins based on percentage buzz change between the last two runs.</li>
        </ul>
        <h4>Feature Roadmap</h4>
        <ul style={{ listStyle: 'circle'}}>
        <li>Mouse hover data</li>
        <li>Table data with clickable links to get coin history</li>
        <li>Filters to manipulate chart</li>
        <li>Email alerts</li>
        <li>Sentiment analysis</li>
        <li>NFT feature set</li>
        </ul>
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