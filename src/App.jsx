import { useState } from 'react'
import { Activity, Play, CheckCircle, AlertCircle, Clock } from 'lucide-react'

function App() {
    const [loading, setLoading] = useState(false)
    const [result, setResult] = useState(null)

    const handleBump = async () => {
        setLoading(true)
        setResult(null)
        try {
            const res = await fetch('/api/bump')
            const data = await res.json()
            setResult(data)
        } catch (error) {
            setResult({ status: 'error', message: 'Failed to trigger bump. Backend might be sleeping or unreachable.' })
        } finally {
            setLoading(false)
        }
    }

    return (
        <div className="min-h-screen bg-slate-900 text-slate-100 flex items-center justify-center p-4">
            <div className="max-w-md w-full bg-slate-800 rounded-xl shadow-2xl overflow-hidden border border-slate-700">

                {/* Header */}
                <div className="p-6 bg-slate-850 border-b border-slate-700 flex items-center gap-3">
                    <div className="p-3 bg-indigo-500/10 rounded-lg">
                        <Activity className="w-6 h-6 text-indigo-400" />
                    </div>
                    <div>
                        <h1 className="text-xl font-bold bg-gradient-to-r from-indigo-400 to-cyan-400 bg-clip-text text-transparent">
                            Autobump Bot
                        </h1>
                        <p className="text-sm text-slate-400">Vercel Serverless Edition</p>
                    </div>
                </div>

                {/* Status Card */}
                <div className="p-6 space-y-6">
                    <div className="flex items-center justify-between p-4 bg-slate-700/50 rounded-lg border border-slate-600/50">
                        <div className="flex items-center gap-3">
                            <Clock className="w-5 h-5 text-emerald-400" />
                            <div>
                                <p className="text-sm font-medium text-slate-200">Cron Schedule</p>
                                <p className="text-xs text-slate-400">Every 30 minutes</p>
                            </div>
                        </div>
                        <div className="flex items-center gap-2 px-3 py-1 bg-emerald-500/10 rounded-full border border-emerald-500/20">
                            <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                            <span className="text-xs font-medium text-emerald-400">Active</span>
                        </div>
                    </div>

                    {/* Action Button */}
                    <button
                        onClick={handleBump}
                        disabled={loading}
                        className={`w-full py-3 px-4 rounded-lg font-medium transition-all flex items-center justify-center gap-2
              ${loading
                                ? 'bg-slate-700 text-slate-400 cursor-not-allowed'
                                : 'bg-indigo-600 hover:bg-indigo-500 text-white shadow-lg shadow-indigo-500/20 active:scale-[0.98]'
                            }`}
                    >
                        {loading ? (
                            <>
                                <div className="w-5 h-5 border-2 border-slate-400 border-t-transparent rounded-full animate-spin"></div>
                                Running Bump Cycle...
                            </>
                        ) : (
                            <>
                                <Play className="w-5 h-5 fill-current" />
                                Trigger Manual Bump
                            </>
                        )}
                    </button>

                    {/* Logs / Result */}
                    {result && (
                        <div className={`p-4 rounded-lg border ${result.status === 'success'
                                ? 'bg-emerald-500/10 border-emerald-500/20'
                                : 'bg-red-500/10 border-red-500/20'
                            }`}>
                            <div className="flex items-center gap-2 mb-2">
                                {result.status === 'success' ? (
                                    <CheckCircle className="w-5 h-5 text-emerald-400" />
                                ) : (
                                    <AlertCircle className="w-5 h-5 text-red-400" />
                                )}
                                <span className={`font-medium ${result.status === 'success' ? 'text-emerald-400' : 'text-red-400'
                                    }`}>
                                    {result.status === 'success' ? 'Bump Cycle Complete' : 'Error'}
                                </span>
                            </div>

                            {result.bumped !== undefined && (
                                <p className="text-sm text-slate-300 ml-7">
                                    Successfully bumped in <span className="text-white font-bold">{result.bumped}</span> channels.
                                </p>
                            )}

                            {result.errors && result.errors.length > 0 && (
                                <div className="mt-2 ml-7 space-y-1">
                                    {result.errors.map((err, i) => (
                                        <p key={i} className="text-xs text-red-300 font-mono">• {err}</p>
                                    ))}
                                </div>
                            )}

                            {result.message && (
                                <p className="text-sm text-slate-300 ml-7">{result.message}</p>
                            )}
                        </div>
                    )}
                </div>

                {/* Footer */}
                <div className="px-6 py-4 bg-slate-850 border-t border-slate-700 flex justify-between items-center text-xs text-slate-500">
                    <span>v2.0.0 (Vercel)</span>
                    <span>Powered by React + Python</span>
                </div>
            </div>
        </div>
    )
}

export default App
