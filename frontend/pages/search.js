import Head from 'next/head'
import Image from 'next/image'
import  Layout  from '../src/components/layout/Layout'
import styles from '../styles/Home.module.css'
import Search from '../src/components/layout/Search'
import axios  from 'axios'
export default function Index({data}) {
  console.log("jobs data",data);
  return (
    <Layout title='Search Your Jobs'>
      <Search data={data}/>
    </Layout>
  )
}