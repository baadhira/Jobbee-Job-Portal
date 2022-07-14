import Head from 'next/head'
import Image from 'next/image'
import  Layout  from '../src/components/layout/Layout'
import styles from '../styles/Home.module.css'
import TopicStats from '../src/components/stats/TopicStats'
import axios  from 'axios'
export default function TopicStatsPage() {
  return (
    <Layout title="Get Topic Stats">
      <TopicStats/>
    </Layout>
  )
}