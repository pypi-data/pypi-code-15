"""DataTable.py


INTRODUCTION

This class is useful for representing a table of data arranged by named
columns, where each row in the table can be thought of as a record:

    name   phoneNumber
    ------ -----------
    Chuck  893-3498
    Bill   893-0439
    John   893-5901

This data often comes from delimited text files which typically
have well defined columns or fields with several rows each of which can
be thought of as a record.

Using a DataTable can be as easy as using lists and dictionaries:

    table = DataTable('users.csv')
    for row in table:
        print row['name'], row['phoneNumber']

Or even:

    table = DataTable('users.csv')
    for row in table:
        print '%(name)s %(phoneNumber)s' % row

The above print statement relies on the fact that rows can be treated
like dictionaries, using the column headings as keys.

You can also treat a row like an array:

    table = DataTable('something.tabbed', delimiter='\t')
    for row in table:
        for item in row:
            print item,
        print


COLUMNS

Column headings can have a type specification like so:
    name, age:int, zip:int

Possible types include string, int, float and datetime.

String is assumed if no type is specified but you can set that
assumption when you create the table:

    table = DataTable(headings, defaultType='float')

Using types like int and float will cause DataTable to actually
convert the string values (perhaps read from a file) to these types
so that you can use them in natural operations. For example:

    if row['age'] > 120:
        self.flagData(row, 'age looks high')

As you can see, each row can be accessed as a dictionary with keys
according the column headings. Names are case sensitive.


ADDING ROWS

Like Python lists, data tables have an append() method. You can append
TableRecords, or you pass a dictionary, list or object, in which case a
TableRecord is created based on given values. See the method docs below
for more details.


FILES

By default, the files that DataTable reads from are expected to be
comma-separated value files.

Limited comments are supported: A comment is any line whose very first
character is a #. This allows you to easily comment out lines in your
data files without having to remove them.

Whitespace around field values is stripped.

You can control all this behavior through the arguments found in the
initializer and the various readFoo() methods:

    ...delimiter=',', allowComments=True, stripWhite=True

For example:

    table = DataTable('foo.tabbed', delimiter='\t',
        allowComments=False, stripWhite=False)

You should access these parameters by their name since additional ones
could appear in the future, thereby changing the order.

If you are creating these text files, we recommend the
comma-separated-value format, or CSV. This format is better defined
than the tab delimited format, and can easily be edited and manipulated
by popular spreadsheets and databases.


MICROSOFT EXCEL

On Microsoft Windows systems with Excel and the win32all package
(http://starship.python.net/crew/mhammond/), DataTable will use Excel
(via COM) to read ".xls" files.

from MiscUtils import DataTable
assert DataTable.canReadExcel()
table = DataTable.DataTable('foo.xls')

With consistency to its CSV processing, DataTable will ignore any row
whose first cell is '#' and strip surrounding whitespace around strings.


TABLES FROM SCRATCH

Here's an example that constructs a table from scratch:

    table = DataTable(['name', 'age:int'])
    table.append(['John', 80])
    table.append({'name': 'John', 'age': 80})
    print table


QUERIES

A simple query mechanism is supported for equality of fields:

    matches = table.recordsEqualTo({'uid': 5})
    if matches:
        for match in matches:
            print match
    else:
        print 'No matches.'


COMMON USES

  * Programs can keep configuration and other data in simple comma-
    separated text files and use DataTable to access them. For example, a
    web site could read its sidebar links from such a file, thereby allowing
    people who don't know Python (or even HTML) to edit these links without
    having to understand other implementation parts of the site.

  * Servers can use DataTable to read and write log files.


FROM THE COMMAND LINE

The only purpose in invoking DataTable from the command line is to see
if it will read a file:

  > python DataTable.py foo.csv

The data table is printed to stdout.


CACHING

DataTable uses "pickle caching" so that it can read .csv files faster
on subsequent loads. You can disable this across the board with:
    from MiscUtils.DataTable import DataTable
    DataTable._usePickleCache = False

Or per instance by passing "usePickleCache=False" to the constructor.

See the docstring of PickleCache.py for more information.


MORE DOCS

Some of the methods in this module have worthwhile doc strings to look at.
See below.


TO DO

  * Allow callback parameter or setting for parsing CSV records.
  * Perhaps TableRecord should inherit list and dict and override
    methods as appropriate?
  * _types and _blankValues aren't really packaged, advertised or
    documented for customization by the user of this module.
  * DataTable:
      * Parameterize the TextColumn class.
      * Parameterize the TableRecord class.
      * More list-like methods such as insert()
      * writeFileNamed() is flawed: it doesn't write the table column type
      * Should it inherit from list?
  * Add error checking that a column name is not a number (which could
    cause problems).
  * Reading Excel sheets with xlrd, not only with win32com.
"""


import os
import sys

from datetime import date, datetime, time, timedelta, tzinfo
from decimal import Decimal

from CSVParser import CSVParser
from CSVJoiner import joinCSVFields
from Funcs import positiveId
from MiscUtils import NoDefault


## Types and blank Values ##

_types = {
    'str': str,
    'string': str,
    'unicode': unicode,
    'basestring': basestring,
    'int': int,
    'bool': bool,
    'long': long,
    'decimal': Decimal,
    'float': float,
    'date': date,
    'datetime': datetime,
    'time': time,
    'timedelta': timedelta,
    'tzinfo': tzinfo
}

_blankValues = {
    str: '',
    unicode: u'',
    basestring: '',
    bool: False,
    int: 0,
    long: 0L,
    float: 0.0,
    Decimal: Decimal('0')
}


## Functions ##

def canReadExcel():
    try:
        from win32com.client import Dispatch
        Dispatch("Excel.Application")
    except Exception:
        return False
    else:
        return True


## Classes ##


class DataTableError(Exception):
    """Data table error."""


class TableColumn(object):
    """Representation of a table column.

    A table column represents a column of the table including name and type.
    It does not contain the actual values of the column. These are stored
    individually in the rows.
    """

    def __init__(self, spec):
        """Initialize the table column.

        The spec parameter is a string such as 'name' or 'name:type'.
        """
        if ':' not in spec:
            name, type = spec, None
        else:
            name, type = spec.split(':', 1)
        self._name = name
        self.setType(type)

    def name(self):
        return self._name

    def type(self):
        return self._type

    def setType(self, type):
        """Set the type (by a string containing the name) of the heading.

        Usually invoked by DataTable to set the default type for columns
        whose types were not specified.
        """
        if type:
            try:
                self._type = _types[type.lower()]
            except Exception:
                raise DataTableError(
                    'Unknown type %r. types=%r' % (type, _types.keys()))
        else:
            self._type = None

    def __repr__(self):
        return '<%s %r with %r at %x>' % (self.__class__.__name__,
            self._name, self._type, positiveId(self))

    def __str__(self):
        return self._name


    ## Utilities ##

    def valueForRawValue(self, value):
        """Set correct type for raw value.

        The rawValue is typically a string or value already of the appropriate
        type. TableRecord invokes this method to ensure that values (especially
        strings that come from files) are the correct types (e.g., ints are
        ints and floats are floats).
        """
        if self._type:
            if isinstance(value, unicode) and self._type is str:
                return value.encode('utf-8')
            elif isinstance(value, str) and self._type is unicode:
                try:
                    return value.decode('utf-8')
                except UnicodeDecodeError:
                    return value.decode('latin-1')
            elif value == '' and self._type in (int, long, float, Decimal):
                value = '0'
            if not isinstance(value, self._type):
                value = self._type(value)
        return value


class DataTable(object):
    """Representation of a data table.

    See the doc string for this module.
    """

    _usePickleCache = True


    ## Init ##

    def __init__(self, filenameOrHeadings=None, delimiter=',',
            allowComments=True, stripWhite=True,
            defaultType=None, usePickleCache=None):
        if usePickleCache is None:
            self._usePickleCache = self._usePickleCache
        else:
            self._usePickleCache = usePickleCache
        if defaultType and defaultType not in _types:
            raise DataTableError(
                'Unknown type for default type: %r' % defaultType)
        self._defaultType = defaultType
        self._filename = None
        self._headings = []
        self._rows = []
        if filenameOrHeadings:
            if isinstance(filenameOrHeadings, basestring):
                self.readFileNamed(filenameOrHeadings, delimiter, allowComments, stripWhite)
            else:
                self.setHeadings(filenameOrHeadings)


    ## File I/O ##

    def readFileNamed(self, filename, delimiter=',',
            allowComments=True, stripWhite=True, worksheet=1, row=1, column=1):
        self._filename = filename
        data = None
        if self._usePickleCache:
            from PickleCache import readPickleCache, writePickleCache
            data = readPickleCache(filename, source='MiscUtils.DataTable')
        if data is None:
            if self._filename.lower().endswith('.xls'):
                self.readExcel(worksheet, row, column)
            else:
                with open(self._filename) as f:
                    self.readFile(f, delimiter, allowComments, stripWhite)
            if self._usePickleCache:
                writePickleCache(self, filename, source='MiscUtils.DataTable')
        else:
            self.__dict__ = data.__dict__
        return self

    def readFile(self, file, delimiter=',',
            allowComments=True, stripWhite=True):
        return self.readLines(file.readlines(), delimiter,
            allowComments, stripWhite)

    def readString(self, string, delimiter=',',
            allowComments=True, stripWhite=True):
        return self.readLines(string.splitlines(), delimiter,
            allowComments, stripWhite)

    def readLines(self, lines, delimiter=',',
            allowComments=True, stripWhite=True):
        if self._defaultType is None:
            self._defaultType = 'str'
        haveReadHeadings = False
        parse = CSVParser(fieldSep=delimiter, allowComments=allowComments,
            stripWhitespace=stripWhite).parse
        for line in lines:
            # process a row, either headings or data
            values = parse(line)
            if values:
                if haveReadHeadings:
                    row = TableRecord(self, values)
                    self._rows.append(row)
                else:
                    self.setHeadings(values)
                    haveReadHeadings = True
        if values is None:
            raise DataTableError("Unfinished multiline record.")
        return self

    @staticmethod
    def canReadExcel():
        return canReadExcel()

    def readExcel(self, worksheet=1, row=1, column=1):
        maxBlankRows = 10
        numRowsToReadPerCall = 20
        from win32com.client import Dispatch
        xl = Dispatch("Excel.Application")
        wb = xl.Workbooks.Open(os.path.abspath(self._filename))
        try:
            sh = wb.Worksheets(worksheet)
            sh.Cells(row, column)
            # determine max column
            numCols = 1
            while 1:
                if sh.Cells(row, numCols).Value in (None, ''):
                    numCols -= 1
                    break
                numCols += 1
            if numCols <= 0:
                return

            def strip(x):
                try:
                    return x.strip()
                except Exception:
                    return x

            # read rows of data
            maxCol = chr(ord('A') + numCols - 1)
            haveReadHeadings = False
            rowNum = row
            numBlankRows = 0
            valuesBuffer = {}  # keyed by row number
            while 1:
                try:
                    # grab a single row
                    values = valuesBuffer[rowNum]
                except KeyError:
                    # woops. read buffer is out of fresh rows
                    valuesRows = sh.Range('A%i:%s%i' % (rowNum, maxCol,
                        rowNum + numRowsToReadPerCall - 1)).Value
                    valuesBuffer.clear()
                    j = rowNum
                    for valuesRow in valuesRows:
                        valuesBuffer[j] = valuesRow
                        j += 1
                    values = valuesBuffer[rowNum]
                values = [strip(v) for v in values]
                nonEmpty = [v for v in values if v]
                if nonEmpty:
                    if values[0] != '#':
                        if haveReadHeadings:
                            row = TableRecord(self, values)
                            self._rows.append(row)
                        else:
                            self.setHeadings(values)
                            haveReadHeadings = True
                    numBlankRows = 0
                else:
                    numBlankRows += 1
                    if numBlankRows > maxBlankRows:
                        # consider end of spreadsheet
                        break
                rowNum += 1
        finally:
            wb.Close()

    def save(self):
        self.writeFileNamed(self._filename)

    def writeFileNamed(self, filename):
        with open(filename, 'w') as f:
            self.writeFile(f)

    def writeFile(self, file):
        """Write the table out as a file.

        This doesn't write the column types (like int) back out.

        It's notable that a blank numeric value gets read as zero
        and written out that way. Also, values None are written as blanks.
        """
        # write headings
        file.write(','.join(map(str, self._headings)))
        file.write('\n')

        def valueWritingMapper(item):
            # So that None gets written as a blank and everything else as a string
            if item is None:
                return ''
            elif isinstance(item, unicode):
                return item.encode('utf-8')
            else:
                return str(item)

        # write rows
        for row in self._rows:
            file.write(joinCSVFields(map(valueWritingMapper, row)))
            file.write('\n')

    def commit(self):
        if self._changed:
            self.save()
            self._changed = False


    ## Headings ##

    def heading(self, index):
        if isinstance(index, basestring):
            index = self._nameToIndexMap[index]
        return self._headings[index]

    def hasHeading(self, name):
        return name in self._nameToIndexMap

    def numHeadings(self):
        return len(self._headings)

    def headings(self):
        return self._headings

    def setHeadings(self, headings):
        """Set table headings.

        Headings can be a list of strings (like ['name', 'age:int'])
        or a list of TableColumns or None.
        """
        if not headings:
            self._headings = []
        elif isinstance(headings[0], basestring):
            self._headings = map(TableColumn, headings)
        elif isinstance(headings[0], TableColumn):
            self._headings = list(headings)
        for heading in self._headings:
            if heading.type() is None:
                heading.setType(self._defaultType)
        self.createNameToIndexMap()


    ## Row access (list like) ##

    def __len__(self):
        return len(self._rows)

    def __getitem__(self, index):
        return self._rows[index]

    def append(self, obj):
        """Append an object to the table.

        If obj is not a TableRecord, then one is created,
        passing the object to initialize the TableRecord.
        Therefore, obj can be a TableRecord, list, dictionary or object.
        See TableRecord for details.
        """
        if not isinstance(obj, TableRecord):
            obj = TableRecord(self, obj)
        self._rows.append(obj)
        self._changed = True


    ## Queries ##

    def recordsEqualTo(self, record):
        records = []
        for row in self._rows:
            for key in row:
                if record[key] != row[key]:
                    break
            else:
                records.append(row)
        return records


    ## As a string ##

    def __repr__(self):
        # Initial info
        s = ['DataTable: %s\n%d rows\n' % (self._filename, len(self._rows))]
        # Headings
        s.append('     ')
        s.append(', '.join(map(str, self._headings)))
        s.append('\n')
        # Records
        for i, row in enumerate(self._rows):
            s.append('%3d. ' % i)
            s.append(', '.join(map(str, row)))
            s.append('\n')
        return ''.join(s)


    ## As a dictionary ##

    def dictKeyedBy(self, key):
        """Return a dictionary containing the contents of the table.

        The content is indexed by the particular key. This is useful
        for tables that have a column which represents a unique key
        (such as a name, serial number, etc.).
        """
        content = {}
        for row in self:
            content[row[key]] = row
        return content


    ## Misc access ##

    def filename(self):
        return self._filename

    def nameToIndexMap(self):
        """Speed-up index.

        Table rows keep a reference to this map in order to speed up
        index-by-names (as in row['name']).
        """
        return self._nameToIndexMap


    ## Self utilities ##

    def createNameToIndexMap(self):
        """Create speed-up index.

        Invoked by self to create the nameToIndexMap after the table's
        headings have been read/initialized.
        """
        map = {}
        for i in range(len(self._headings)):
            map[self._headings[i].name()] = i
        self._nameToIndexMap = map


class TableRecord(object):
    """Representation of a table record."""


    ## Init ##

    def __init__(self, table, values=None, headings=None):
        """Initialize table record.

        Dispatches control to one of the other init methods based on the type
        of values. Values can be one of three things:
            1. A TableRecord
            2. A list
            3. A dictionary
            4. Any object responding to hasValueForKey() and valueForKey().
        """
        if headings is None:
            self._headings = table.headings()
        else:
            self._headings = headings
        self._nameToIndexMap = table.nameToIndexMap()
        if values is not None:
            if isinstance(values, (list, tuple)):
                self.initFromSequence(values)
            elif isinstance(values, dict):
                self.initFromDict(values)
            else:
                try:
                    self.initFromObject(values)
                except AttributeError:
                    raise DataTableError('Unknown type for values %r.' % values)

    def initFromSequence(self, values):
        if len(self._headings) < len(values):
            raise DataTableError('There are more values than headings.\n'
                'headings(%d, %s)\nvalues(%d, %s)' % (len(self._headings),
                self._headings, len(values), values))
        self._values = []
        numHeadings = len(self._headings)
        numValues = len(values)
        assert numValues <= numHeadings
        for i in range(numHeadings):
            heading = self._headings[i]
            if i >= numValues:
                self._values.append(_blankValues.get(heading.type()))
            else:
                self._values.append(heading.valueForRawValue(values[i]))

    def initFromDict(self, values):
        self._values = []
        for heading in self._headings:
            name = heading.name()
            if name in values:
                self._values.append(heading.valueForRawValue(values[name]))
            else:
                self._values.append(_blankValues.get(heading.type()))

    def initFromObject(self, obj):
        """Initialize from object.

        The object is expected to response to hasValueForKey(name) and
        valueForKey(name) for each of the headings in the table. It's alright
        if the object returns False for hasValueForKey(). In that case, a
        "blank" value is assumed (such as zero or an empty string). If
        hasValueForKey() returns True, then valueForKey() must return a value.
        """
        self._values = []
        for heading in self._headings:
            name = heading.name()
            if obj.hasValueForKey(name):
                self._values.append(heading.valueForRawValue(
                    obj.valueForKey(name)))
            else:
                self._values.append(_blankValues.get(heading.type()))


    ## Accessing like a sequence or dictionary ##

    def __len__(self):
        return len(self._values)

    def __getitem__(self, key):
        if isinstance(key, basestring):
            key = self._nameToIndexMap[key]
        try:
            return self._values[key]
        except TypeError:
            raise TypeError('key=%r, key type=%r, self._values=%r'
                % (key, type(key), self._values))

    def __setitem__(self, key, value):
        if isinstance(key, basestring):
            key = self._nameToIndexMap[key]
        self._values[key] = value

    def __delitem__(self, key):
        if isinstance(key, basestring):
            key = self._nameToIndexMap[key]
        del self._values[key]

    def __contains__(self, key):
        return key in self._nameToIndexMap

    def __repr__(self):
        return '%s' % self._values

    def __iter__(self):
        for value in self._values:
            yield value

    def get(self, key, default=None):
        index = self._nameToIndexMap.get(key)
        if index is None:
            return default
        else:
            return self._values[index]

    def has_key(self, key):
        return key in self

    def keys(self):
        return self._nameToIndexMap.keys()

    def values(self):
        return self._values

    def items(self):
        items = []
        for key in self._nameToIndexMap:
            items.append((key, self[key]))
        return items

    def iterkeys(self):
        return iter(self._nameToIndexMap)

    def itervalues(self):
        return iter(self)

    def iteritems(self):
        for key in self.self._nameToIndexMap:
            yield key, self[key]


    ## Additional access ##

    def asList(self):
        """Return a sequence whose values are the same as the record's.

        The order of the sequence is the one defined by the table.
        """
        # It just so happens that our implementation already has this
        return self._values[:]

    def asDict(self):
        """Return a dictionary whose key-values match the table record."""
        record = {}
        nameToIndexMap = self._nameToIndexMap
        for key in nameToIndexMap:
            record[key] = self._values[nameToIndexMap[key]]
        return record


    ## valueForFoo() family ##

    def valueForKey(self, key, default=NoDefault):
        if default is NoDefault:
            return self[key]
        else:
            return self.get(key, default)

    def valueForAttr(self, attr, default=NoDefault):
        return self.valueForKey(attr['Name'], default)


def main(args=None):
    if args is None:
        args = sys.argv
    for arg in args[1:]:
        dt = DataTable(arg)
        print '*** %s ***' % arg
        print dt
        print


if __name__ == '__main__':
    main()
