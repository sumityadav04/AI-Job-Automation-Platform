import React from 'react'

// AI Job Automation Platform - Single-file React component (TailwindCSS + shadcn/ui style)
// Default export: LandingPage

export default function LandingPage() {
  return (
    <main className="min-h-screen bg-gradient-to-b from-white to-gray-50 text-slate-900">
      <header className="max-w-6xl mx-auto p-6 flex items-center justify-between">
        <div className="flex items-center gap-4">
          <div className="w-10 h-10 bg-gradient-to-br from-indigo-500 to-purple-500 rounded-xl flex items-center justify-center text-white font-semibold">AI</div>
          <div>
            <h1 className="text-lg font-semibold">AI Job Automation</h1>
            <p className="text-xs text-slate-500">Hire faster. Smarter. Automatically.</p>
          </div>
        </div>
        <nav className="hidden md:flex gap-6 items-center text-sm">
          <a className="hover:text-indigo-600" href="#features">Features</a>
          <a className="hover:text-indigo-600" href="#pricing">Pricing</a>
          <a className="hover:text-indigo-600" href="#faq">FAQ</a>
          <button className="ml-2 px-4 py-2 rounded-lg border border-indigo-600 text-indigo-600 hover:bg-indigo-50">Sign in</button>
        </nav>
      </header>

      {/* HERO */}
      <section className="max-w-6xl mx-auto px-6 py-12 grid gap-8 md:grid-cols-2 items-center">
        <div>
          <h2 className="text-4xl md:text-5xl font-extrabold leading-tight">Automate your hiring with AI — from posting to offer</h2>
          <p className="mt-4 text-lg text-slate-600">Use intelligent automation to source candidates, screen resumes, schedule interviews, and analyze outcomes — all from a single dashboard.</p>

          <div className="mt-8 flex gap-4 items-center">
            <a href="#contact" className="inline-flex items-center gap-2 px-5 py-3 rounded-lg bg-indigo-600 text-white font-medium shadow">Request a demo</a>
            <a href="#features" className="inline-flex items-center gap-2 px-4 py-3 rounded-lg border">Explore features</a>
          </div>

          <div className="mt-6 flex flex-wrap gap-4 text-sm text-slate-500">
            <div className="p-3 bg-white rounded-lg shadow-sm">Resume parsing • 99.7% accuracy</div>
            <div className="p-3 bg-white rounded-lg shadow-sm">ATS integrations • Workday & Greenhouse</div>
            <div className="p-3 bg-white rounded-lg shadow-sm">Interview scheduling • Calendar sync</div>
          </div>
        </div>

        <div className="relative">
          <div className="rounded-2xl bg-gradient-to-br from-indigo-50 to-white p-6 shadow-xl">
            <div className="flex items-center justify-between">
              <div>
                <div className="text-xs text-slate-500">Open roles</div>
                <div className="text-2xl font-semibold mt-1">42</div>
              </div>
              <div className="text-right">
                <div className="text-xs text-slate-500">Avg time-to-hire</div>
                <div className="text-2xl font-semibold mt-1">12 days</div>
              </div>
            </div>

            <div className="mt-6 bg-white p-4 rounded-xl">
              <div className="text-sm text-slate-600">Candidate pipeline</div>
              <div className="mt-3 grid grid-cols-3 gap-3 text-xs">
                <div className="p-3 border rounded">Sourced<br/><span className="text-lg font-semibold">1,204</span></div>
                <div className="p-3 border rounded">Screened<br/><span className="text-lg font-semibold">248</span></div>
                <div className="p-3 border rounded">Interviewed<br/><span className="text-lg font-semibold">86</span></div>
              </div>
            </div>

            <div className="mt-4 text-xs text-slate-500">Live integrations: Slack • Gmail • Zoom</div>
          </div>
        </div>
      </section>

      {/* FEATURES */}
      <section id="features" className="max-w-6xl mx-auto px-6 py-12">
        <h3 className="text-2xl font-bold">Platform highlights</h3>
        <p className="text-slate-600 mt-2">Everything you need to reduce time-to-hire and improve candidate quality.</p>

        <div className="mt-8 grid gap-6 md:grid-cols-3">
          <FeatureCard title="Smart Sourcing" desc="Auto-source candidates across job boards and social networks using intent and skill signals."/>
          <FeatureCard title="Resume Intelligence" desc="Extract skills, experience, and role-fit scores from resumes with NLP and structured parsing."/>
          <FeatureCard title="Automated Screening" desc="Run role-specific screening workflows and automated assessments before interviews."/>
          <FeatureCard title="Interview Orchestration" desc="Auto-schedule interviews, send reminders, and record outcomes with calendar sync."/>
          <FeatureCard title="ATS & HRIS Integrations" desc="Two-way sync with popular systems (Workday, Greenhouse, BambooHR) and webhooks for custom flows."/>
          <FeatureCard title="Analytics & Bias Checks" desc="Data-driven hiring analytics and built-in bias detection reports for fairer hiring."/>
        </div>
      </section>

      {/* HOW IT WORKS */}
      <section className="max-w-6xl mx-auto px-6 py-12 bg-white rounded-xl shadow-sm">
        <h4 className="text-xl font-bold">How it works</h4>
        <ol className="mt-6 grid gap-4 md:grid-cols-4 text-slate-600">
          <li className="p-4 border rounded-lg">1. Connect sources (job boards, careers page)</li>
          <li className="p-4 border rounded-lg">2. Auto-parse resumes & score candidates</li>
          <li className="p-4 border rounded-lg">3. Run automated screens & interviews</li>
          <li className="p-4 border rounded-lg">4. Hire, onboard & analyze</li>
        </ol>
      </section>

      {/* PRICING */}
      <section id="pricing" className="max-w-6xl mx-auto px-6 py-12">
        <h3 className="text-2xl font-bold">Pricing</h3>
        <p className="text-slate-600 mt-2">Simple pricing for teams of any size. Annual plans include priority support and onboarding.</p>

        <div className="mt-8 grid gap-6 md:grid-cols-3">
          <PriceCard tier="Starter" price="$99/mo" perks={["Up to 5 roles","Resume parsing","Email support"]} />
          <PriceCard tier="Growth" price="$299/mo" perks={["Up to 50 roles","ATS integrations","Priority support"]} popular />
          <PriceCard tier="Enterprise" price="Contact us" perks={["Unlimited roles","Custom integrations","Dedicated CSM"]} />
        </div>
      </section>

      {/* CTA + CONTACT */}
      <section id="contact" className="max-w-6xl mx-auto px-6 py-12 bg-gradient-to-r from-indigo-600 to-purple-600 text-white rounded-2xl">
        <div className="md:flex md:items-center md:justify-between">
          <div>
            <h4 className="text-2xl font-bold">Ready to automate hiring?</h4>
            <p className="mt-2 text-slate-100">Book a demo or start a free trial — no credit card required.</p>
          </div>

          <form className="mt-6 md:mt-0 flex gap-3">
            <input aria-label="Email" type="email" placeholder="Your work email" className="px-4 py-3 rounded-lg text-slate-800" />
            <button className="px-5 py-3 rounded-lg bg-white text-indigo-600 font-semibold">Get started</button>
          </form>
        </div>

        <div className="mt-6 text-sm opacity-80">By submitting you agree to our terms. We care about candidate privacy and data security.</div>
      </section>

      {/* FAQ */}
      <section id="faq" className="max-w-6xl mx-auto px-6 py-12">
        <h3 className="text-2xl font-bold">FAQ</h3>
        <div className="mt-6 grid gap-4 md:grid-cols-2 text-slate-600">
          <FAQItem q="Do you support GDPR / data residency?" a="Yes — we support data residency options and deletion endpoints for candidate data." />
          <FAQItem q="Can I use my own assessment tests?" a="Yes — plug in third-party assessments or use our built-in tests." />
          <FAQItem q="How secure is candidate data?" a="Encrypted at rest and in transit; SOC2-ready controls and role-based access." />
          <FAQItem q="Do you offer custom integrations?" a="Yes — our Enterprise plan includes custom integrations and a dedicated CSM." />
        </div>
      </section>

      <footer className="max-w-6xl mx-auto px-6 py-8 text-sm text-slate-500 flex justify-between">
        <div>© {new Date().getFullYear()} AI Job Automation</div>
        <div className="flex gap-4">Privacy • Terms • Contact</div>
      </footer>
    </main>
  )
}


/* ------------------------- Components --------------------------- */
function FeatureCard({ title, desc }){
  return (
    <div className="p-6 bg-white border rounded-lg shadow-sm">
      <div className="text-indigo-600 font-semibold">{title}</div>
      <div className="mt-2 text-sm text-slate-600">{desc}</div>
      <div className="mt-4 text-xs text-slate-400">Enterprise-grade • Scalable</div>
    </div>
  )
}

function PriceCard({ tier, price, perks, popular }){
  return (
    <div className={`p-6 rounded-lg border ${popular ? 'border-indigo-600 shadow-lg' : 'bg-white'}`}>
      <div className="flex items-center justify-between">
        <div className="text-lg font-semibold">{tier}</div>
        {popular && <div className="text-xs px-2 py-1 bg-indigo-100 text-indigo-700 rounded">Popular</div>}
      </div>
      <div className="mt-4 text-2xl font-bold">{price}</div>
      <ul className="mt-4 text-sm space-y-2">
        {perks.map((p,i)=> <li key={i}>• {p}</li>)}
      </ul>
      <div className="mt-6">
        <button className={`w-full px-4 py-3 rounded-lg ${popular ? 'bg-indigo-600 text-white' : 'border'}`}>Choose</button>
      </div>
    </div>
  )
}

function FAQItem({ q, a }){
  return (
    <details className="p-4 border rounded-lg">
      <summary className="font-medium">{q}</summary>
      <div className="mt-2 text-sm text-slate-600">{a}</div>
    </details>
  )
}

