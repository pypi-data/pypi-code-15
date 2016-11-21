import re
from os.path import dirname, join
from collections import defaultdict
from operator import itemgetter
from six.moves.urllib.parse import quote

from dark.html import NCBISequenceLinkURL


class ProteinGrouper(object):
    """
    Group matched proteins by the virus they come from.

    @param assetDir: The C{str} directory name where
        C{noninteractive-alignment-panel.py} put its HTML, blue plot and
        alignment panel images, and FASTA files. This must be relative
        to the filenames that will later be passed to C{addFile}.
    @param sampleNameRegex: A C{str} regular expression that can be used to
        extract a short sample name from full file names subsequently passed
        to C{self.addFile}. The regular expression must have a matching group
        (delimited by parentheses) to capture the part of the file name that
        should be used as the sample name.
    """

    # The following regex is deliberately greedy (using .*) to consume the
    # whole protein title before backtracking to find the last [virus title]
    # section. That way, it will match just the last [virus title] in a
    # protein. This avoids situations in which two [...] delimited substrings
    # are present in a protein name (in which case we just want the last).
    # E.g., the following is a complete protein name:
    #
    #   gi|19919894|ref|NP_612577.1| Enzymatic polyprotein [Contains: Aspartic
    #   protease; Endonuclease; Reverse transcriptase] [Carnation etched ring
    #   virus]
    #
    # Unfortunately the regex doesn't find the vius title when the protein
    # title has nested [...] sections, as in this example:
    #
    #   gi|224808893|ref|YP_002643049.1| replication-associated protein [Tomato
    #   leaf curl Nigeria virus-[Nigeria:2006]]
    #
    # I decided not to worry about nested [...] sections (there are only 2
    # instances that I know of).
    VIRUS_RE = re.compile('^(.*)\[([^\]]+)\]$')

    # The virus title assigned to proteins whose title strings cannot be parsed
    # for a virus title (see previous comment).  Do not use '<', '>' or any
    # other HTML special chars in the following.
    NO_VIRUS_TITLE = '[no virus name found in protein title]'

    VIRALZONE = 'http://viralzone.expasy.org/cgi-bin/viralzone/search?query='

    def __init__(self, assetDir='out', sampleNameRegex=None):
        self._sampleNameRegex = (re.compile(sampleNameRegex) if sampleNameRegex
                                 else None)
        self._assetDir = assetDir
        # virusTitles is a dict of dicts of lists.
        self.virusTitles = defaultdict(lambda: defaultdict(list))
        # sampleNames is keyed by sample name and will have values that hold
        # the sample's alignment panel index.html file.
        self.sampleNames = {}

    def _title(self):
        """
        Create a title summarizing the viruses and samples.

        @return: A C{str} title.
        """
        return (
            '%d virus%s found in %d sample%s' %
            (len(self.virusTitles), '' if len(self.virusTitles) == 1 else 'es',
             len(self.sampleNames), '' if len(self.sampleNames) == 1 else 's'))

    def addFile(self, filename, fp):
        """
        Read and record protein information for a sample.

        @param filename: A C{str} file name.
        @param fp: An open file pointer to read the file's data from.
        """

        if self._sampleNameRegex:
            match = self._sampleNameRegex.search(filename)
            if match:
                sampleName = match.group(1)
            else:
                sampleName = filename
        else:
            sampleName = filename

        outDir = join(dirname(filename), self._assetDir)

        self.sampleNames[sampleName] = join(outDir, 'index.html')

        for index, proteinLine in enumerate(fp):
            proteinLine = proteinLine[:-1]
            (coverage, medianScore, bestScore, readCount, hspCount,
             proteinLength, titles) = proteinLine.split(None, 6)

            match = self.VIRUS_RE.match(titles)
            if match:
                proteinTitle = match.group(1).strip()
                virusTitle = match.group(2)
            else:
                proteinTitle = titles
                virusTitle = self.NO_VIRUS_TITLE

            self.virusTitles[virusTitle][sampleName].append({
                'bestScore': float(bestScore),
                'bluePlotFilename': join(outDir, '%d.png' % index),
                'coverage': float(coverage),
                'fastaFilename': join(outDir, '%d.fasta' % index),
                'hspCount': int(hspCount),
                'index': index,
                'medianScore': float(medianScore),
                'proteinLength': int(proteinLength),
                'proteinTitle': proteinTitle,
                'proteinURL': NCBISequenceLinkURL(proteinTitle),
                'readCount': int(readCount),
            })

    def toStr(self):
        """
        Produce a string representation of the virus summary.

        @return: A C{str} suitable for printing.
        """
        titleGetter = itemgetter('proteinTitle')
        readCountGetter = itemgetter('readCount')
        result = []
        append = result.append

        append(self._title())
        append('')

        for virusTitle in sorted(self.virusTitles):
            samples = self.virusTitles[virusTitle]
            sampleCount = len(samples)
            append('%s (in %d sample%s)' %
                   (virusTitle,
                    sampleCount, '' if sampleCount == 1 else 's'))
            for sampleName in sorted(samples):
                proteins = samples[sampleName]
                proteinCount = len(proteins)
                totalReads = sum(readCountGetter(p) for p in proteins)
                append('  %s (%d protein%s, %d read%s)' %
                       (sampleName,
                        proteinCount, '' if proteinCount == 1 else 's',
                        totalReads, '' if totalReads == 1 else 's'))
                proteins.sort(key=titleGetter)
                for proteinMatch in proteins:
                    append(
                        '    %(coverage).2f\t%(medianScore).2f\t'
                        '%(bestScore).2f\t%(readCount)4d\t%(hspCount)4d\t'
                        '%(index)3d\t%(proteinTitle)s'
                        % proteinMatch)
            append('')

        return '\n'.join(result)

    def toHTML(self):
        """
        Produce an HTML string representation of the virus summary.

        @return: An HTML C{str} suitable for printing.
        """
        titleGetter = itemgetter('proteinTitle')
        readCountGetter = itemgetter('readCount')
        virusTitles = sorted(self.virusTitles)
        sampleNames = sorted(self.sampleNames)

        result = [
            '<html>',
            '<head>',
            '<title>',
            self._title(),
            '</title>',
            '</head>',
            '<body>',
            '<style>',
            '''\
            body {
                margin-left: 2%;
                margin-right: 2%;
            }
            .sample {
                margin-bottom: 2px;
            }
            .sample-name {
                color: red;
            }
            .index {
                font-size: small;
            }
            .protein-title {
                font-family: "Courier New", Courier, monospace;
            }
            .stats {
                font-family: "Courier New", Courier, monospace;
                white-space: pre;
            }
            .protein-list {
                margin-top: 2px;
            }''',
            '</style>',
            '</head>',
            '<body>',
        ]

        append = result.append

        append('<h1>%s</h1>' % self._title())

        # Write a linked table of contents by virus.
        append('<h2>Virus index</h2>')
        append('<p class="index">')
        for virusTitle in virusTitles:
            append('<a href="#virus-%s">%s</a>' % (virusTitle, virusTitle))
            append('&middot;')
        # Get rid of final middle dot.
        result.pop()
        append('</p>')

        # Write a linked table of contents by sample.
        append('<h2>Sample index</h2>')
        append('<p class="index">')
        for sampleName in sampleNames:
            append('<a href="#sample-%s">%s</a>' % (sampleName, sampleName))
            append('&middot;')
        # Get rid of final middle dot.
        result.pop()
        append('</p>')

        # Write all viruses (with samples (with proteins)).
        append('<h1>Viruses by sample</h1>')
        for virusTitle in virusTitles:
            samples = self.virusTitles[virusTitle]
            sampleCount = len(samples)
            append(
                '<a id="virus-%s">'
                '<h2 class="virus"><span class="virus-title">%s</span> '
                '(in %d sample%s, <a href="%s%s">viralzone</a>)</h2>' %
                (virusTitle, virusTitle, sampleCount,
                 '' if sampleCount == 1 else 's',
                 self.VIRALZONE, quote(virusTitle)))
            for sampleName in sorted(samples):
                proteins = samples[sampleName]
                proteinCount = len(proteins)
                totalReads = sum(readCountGetter(p) for p in proteins)
                append(
                    '<p class=sample>'
                    '<span class="sample-name">%s</span> '
                    '(%d protein%s, %d read%s, <a href="%s">panel</a>)' %
                    (sampleName,
                     proteinCount, '' if proteinCount == 1 else 's',
                     totalReads, '' if totalReads == 1 else 's',
                     self.sampleNames[sampleName]))
                proteins.sort(key=titleGetter)
                append('<ul class="protein-list">')
                for proteinMatch in proteins:
                    append(
                        '<li>'
                        '<span class="stats">'
                        '%(coverage).2f %(medianScore).2f %(bestScore).2f '
                        '%(readCount)4d %(hspCount)4d %(index)3d '
                        '</span> '
                        '<span class="protein-title">'
                        '%(proteinTitle)s'
                        '</span> '
                        '(<a href="%(bluePlotFilename)s">blue plot</a>, '
                        '<a href="%(fastaFilename)s">fasta</a>'
                        % proteinMatch)

                    if proteinMatch['proteinURL']:
                        # Append this directly to the last string in result, to
                        # avoid introducing whitespace when we join result
                        # using '\n'.
                        result[-1] += (', <a href="%s">NCBI</a>' %
                                       proteinMatch['proteinURL'])
                    result[-1] += ')'

                    append('</li>')

                append('</ul>')
                append('</p>')

        # Write all samples (with viruses (with proteins)).
        append('<h1>Samples by virus</h1>')
        for sampleName in sorted(sampleNames):

            sampleVirusTitles = set()
            for virusTitle in virusTitles:
                if sampleName in self.virusTitles[virusTitle]:
                    sampleVirusTitles.add(virusTitle)

            append(
                '<a id="sample-%s">'
                '<h2 class="sample"><span class="sample-name">%s</span> '
                '(has proteins from %d virus%s, <a href="%s">panel</a>)</h2>' %
                (sampleName, sampleName, len(sampleVirusTitles),
                 '' if len(sampleVirusTitles) == 1 else 'es',
                 self.sampleNames[sampleName]))

            for virusTitle in sorted(sampleVirusTitles):
                proteins = self.virusTitles[virusTitle][sampleName]
                proteinCount = len(proteins)
                totalReads = sum(readCountGetter(p) for p in proteins)
                append(
                    '<p class="sample">'
                    '<span class="virus-title">%s</span> '
                    '(%d protein%s, %d read%s)' %
                    (virusTitle,
                     proteinCount, '' if proteinCount == 1 else 's',
                     totalReads, '' if totalReads == 1 else 's'))
                proteins.sort(key=titleGetter)
                append('<ul class="protein-list">')
                for proteinMatch in proteins:
                    append(
                        '<li>'
                        '<span class="stats">'
                        '%(coverage).2f %(medianScore).2f %(bestScore).2f '
                        '%(readCount)4d %(hspCount)4d %(index)3d '
                        '</span> '
                        '<span class="protein-title">'
                        '%(proteinTitle)s'
                        '</span> '
                        '(<a href="%(bluePlotFilename)s">blue plot</a>, '
                        '<a href="%(fastaFilename)s">fasta</a>'
                        % proteinMatch)

                    if proteinMatch['proteinURL']:
                        # Append this directly to the last string in result, to
                        # avoid introducing whitespace when we join result
                        # using '\n'.
                        result[-1] += (', <a href="%s">NCBI</a>' %
                                       proteinMatch['proteinURL'])
                    result[-1] += ')'

                    append('</li>')

                append('</ul>')
                append('</p>')

        append('</body>')
        append('</html>')

        return '\n'.join(result)
