import Head from "next/head";
import Image from "next/image";
import Layout from "../../src/components/layout/Layout";
import NotFound from "../../src/components/layout/NotFound";

import JobDetails from "../../src/components/job/JobDetails";
import axios from "axios";
export default function JobDetailsPage({
  job,
  candidates,
  error,
  access_token,
//   user,
}) {
  if (error?.includes("Not found")) return <NotFound />;

  return (
    <Layout title={job.title}>
      <JobDetails
        job={job}
        candidates={candidates}
        access_token={access_token}
      />
    </Layout>
  );
}

export async function getServerSideProps({ req, params }) {
  try {
    const res = await axios.get(
      `${process.env.API_URL}/api/jobs/${params.id}/`
    );

    const job = res.data.job;
    const candidates = res.data.candidates;

    const access_token = req.cookies.access || "";

    return {
      props: {
        job,
        candidates,
        access_token,
      },
    };
  } catch (error) {
    return {
      props: {
        error: error.response.data.detail,
      },
    };
  }
}
