import cookie from 'cookie'
import axios  from 'axios'
export default async(req,res) => {

    if(req.method==='GET'){
        const {username,password} = req.body;

        const cookies=cookie.parse(req.headers.cookie || '')

        const access=cookies.access || false

        if(!access){
            return res.status(401).json({
                message: 'Login first to load user'
            })
        }



        try {
            const response = await axios.get(`${process.env.API_URL}/api/me/`,
            {
                    headers:{
                    'Authorization':`Bearer ${access}`
                }
            })

            if(response.data){
                return res.status(200).json({
                    user: response.data
                })
            }
      
                
        }catch(error) {
            console.log("error.response",error.response);
            res.status(error?.response.status).json({
                error:"Something went wrong while retrieving user",
            })

        }
    }
}