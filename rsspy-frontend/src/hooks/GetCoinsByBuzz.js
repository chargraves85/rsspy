import axios from "axios"

export async function GetCoinsByBuzz() {

     try {
        const res = await axios.post('http://localhost:8000/graphql', {  // TODO: set up env injection
            query: `query MyQuery {
            coinByBuzzChange {
              coinName
              symbol
              data
            }
}`
        });
        return res;
    } catch (err) {
        console.log(err);
        return await Promise.reject(err);
    }
};