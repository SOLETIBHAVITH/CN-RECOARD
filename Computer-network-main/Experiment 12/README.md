# Experiment 12 - Analysis of RTP Packet Delay and Loss Using Wireshark

Aim:

To inspect RTP sequence numbers, arrival timing, jitter and apparent packet loss using Wireshark stream analysis.

Procedure:

1. Obtain an authorized RTP test capture. A public example is linked from the official Wireshark RTP page below; do not record or publish private calls.
2. Open the capture using File > Open and apply display filter `rtp`.
3. If known RTP traffic appears only as UDP, select its authorized UDP stream and use Analyze > Decode As > RTP. Only force decoding when the stream format is known to be RTP.
4. Expand an RTP header and inspect sequence number, timestamp, payload type and SSRC.
5. Open Telephony > RTP > RTP Streams, select the intended direction/SSRC, then Analyze; or select an RTP packet and open Telephony > RTP > RTP Stream Analysis.
6. Inspect per-packet sequence, Delta, Jitter and status, together with the stream's packet count, inferred lost packets and duration. Menu wording can vary by installed version.
7. Check sequence wraparound, late/out-of-order packets, duplicates and capture loss before interpreting gaps as network loss.
8. Record only actual measurements and explain the timing limits below. Keep captures outside this public repository.

Program / Commands:

Wireshark display filters:

```text
rtp
rtp && udp.port == 5004
rtp && rtp.ssrc == 0x12345678
rtp.seq == 1000
```

The port, SSRC and sequence above are example selectors, not observed values. Replace them with fields from the authorized capture. Useful fields include `rtp.seq`, `rtp.timestamp`, `rtp.ssrc` and `frame.time_delta_displayed`.

Interpretation:

- Sequence numbers help detect apparent missing packets; they wrap modulo 65536. Reordering, capture loss and incomplete capture boundaries can also produce misleading gaps.
- Delta is a difference between captured packet arrival times at the capture point. `frame.time_delta_displayed` depends on the current display filter and can mix streams unless the filter isolates one stream.
- RTP timestamps use the media clock, not necessarily milliseconds. Interpret their increments using the payload/codec clock rate.
- RTP interarrival jitter estimates variation in relative transit timing. It is not an absolute one-way latency measurement.
- A single ordinary capture generally cannot establish accurate one-way network delay. That needs appropriately synchronized endpoints and sender/receiver timing information. RTCP timing can support additional analysis when available.

Output / Observation:

**Execution Status: Not Verified**

Wireshark was unavailable and no RTP capture was analyzed. Stream counts, sequence gaps, jitter, loss percentages and delay measurements are therefore not supplied. No capture file or private communication is included.

References: [Wireshark RTP and public sample links](https://wiki.wireshark.org/RTP), [RTP field reference](https://www.wireshark.org/docs/dfref/r/rtp.html), [RTP stream analysis guide](https://www.wireshark.org/docs/wsug_html_chunked/ChTelRTP.html), [RTP timing specification, RFC 3550](https://www.rfc-editor.org/rfc/rfc3550).
