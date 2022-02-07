import axios from "axios"

export async function GetCoinsByBuzz() {

     try {
        const res = await axios.post('http://backend:8000/graphql', {  // TODO: set up env injection
            query: `query MyQuery {
            coinByBuzzChange {
              coinName
              symbol
              data
            }
}`
        });
        console.log('******************************************************************')
        console.log(res)
        console.log('******************************************************************')
        return res;
    } catch (err) {
        console.log(err);
        return await Promise.reject(err);
    }
};