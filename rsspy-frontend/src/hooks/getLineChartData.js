import { GetCoinsByBuzz } from "./GetCoinsByBuzz"

export async function getLineChartData() {

    const chartData = await GetCoinsByBuzz().then((response) => {

        const fulldataset = response.data.data
        const dataset = fulldataset.coinByBuzzChange.slice(0, 10)

        const data = {};
        data.labels = [];
        data.datasets = [];

        const colors = [
            'rgb(26, 188, 156)',
            'rgb(230, 126, 34)',
            'rgb(231, 76, 60)',
            'rgb(52, 152, 219)',
            'rgb(52, 73, 94)',
            'rgb(149, 165, 166)',
            'rgb(179, 55, 113)',
            'rgb(252, 66, 123)',
            'rgb(189, 197, 129)',
            'rgb(214, 162, 232)',
        ]

        var colorPicker = 0

        const unsortedLabels = []

        const allTimestamps = Object.keys(JSON.parse(dataset[0].data))
        allTimestamps.forEach(timestamp => {

            var date = new Date(timestamp * 1000);

            const formattedDate = (date.getMonth() + 1) +
                "/" + date.getDate() +
                "/" + date.getFullYear() +
                " " + date.getHours() +
                ":" + date.getMinutes() +
                ":" + date.getSeconds()


            unsortedLabels.push(formattedDate)
        })

        data.labels = unsortedLabels.sort()

        dataset.forEach(element => {

            const label = element.coinName;
            const elementDataSet = []
            const keys = Object.keys(JSON.parse(element.data))
            const elementDataJson = JSON.parse(element.data)
            const buzzArray = []

            keys.forEach(key => {
                elementDataSet.push(elementDataJson[key].buzzScore)
                buzzArray.push(elementDataJson[key].buzzScore)
            })

            const consecutiveDifference = arr => {
                const res = [];
                for (let i = 0; i < arr.length; i++) {
                    if (arr[i + 1]) {
                        res.push(
                            (arr[i + 1] - arr[i]) / arr[i] * 100);
                    };
                };
                return res;
            };

            const pctData = consecutiveDifference(buzzArray)
            pctData.unshift(0)

            data.datasets.push({
                label: label,
                data: pctData,  // uncomment to graph percent changes
                // data: elementDataSet,  // uncomment to graph pure buzzScore
                borderColor: colors[colorPicker]
            });

            colorPicker += 1

        });

        return data
    })

    return chartData;
};

export default getLineChartData;
