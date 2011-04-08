==========================
Telecom Log Service Client
==========================

Telecom Log Service Client (``tlscli``) is a Python command-line client for
CORBA Telecom Log Service.

Using you can:

* create a new log
* query a log
* add or remove log records

For more information on the TelecomLogService, see:
  http://www.omg.org/spec/TLOG/

The project is hosted on Launchpad:
  https://launchpad.net/tlscli

Example
=======
Here's an example session, assuming a Telecom Log Service is running::

    me@mymachine$ tlscli -ORBInitRef LogMgr=`cat /var/run/corba/tls.ior` list
    me@mymachine$ tlscli -ORBInitRef LogMgr=`cat /var/run/corba/tls.ior` create
    0
    me@mymachine$ tlscli -ORBInitRef LogMgr=`cat /var/run/corba/tls.ior` list
    0
    me@mymachine$ tlscli -ORBInitRef LogMgr=`cat /var/run/corba/tls.ior` info 0
    id: 0
    QoS: none
    max-record-life: infinite
    max-size: unlimited
    current-size: 56 bytes
    records: 1
    log-full-action: wrap
    administrative-state: unlocked
    forwarding-state: on
    operational-state: enabled
    interval: now - forever
    availability-status: { off-duty: False; full: False }
    capacity-alarm-thresholds: [100]
    week-mask: 
    ------------------------------------------------------------------------------
    me@mymachine$ tlscli -ORBInitRef LogMgr=`cat /var/run/corba/tls.ior` write 'Hello world!' to 0
    me@mymachine$ tlscli -ORBInitRef LogMgr=`cat /var/run/corba/tls.ior` info 0
    id: 0
    QoS: none
    max-record-life: infinite
    max-size: unlimited
    current-size: 57 bytes
    records: 1
    log-full-action: wrap
    administrative-state: unlocked
    forwarding-state: on
    operational-state: enabled
    interval: now - forever
    availability-status: { off-duty: False; full: False }
    capacity-alarm-thresholds: [100]
    week-mask: 
    ------------------------------------------------------------------------------
    me@mymachine$ tlscli -ORBInitRef LogMgr=`cat /var/run/corba/tls.ior` retrieve 10 after `date +%Y%m%d` from 0
    id: 1
    time: Sat Dec 25 17:11:57 2010
    attributes: []
    info: Hello world!
    ------------------------------------------------------------------------------


This creates a new log with id 0, then write a new log record to it with text ``Hello world``.

Prerequisites
=============

To install ``tlscli``, you need a working installation of
`omniORBpy <http://omniorb.sourceforge.net/>`_. Indeed CORBA stubs are
generated at install time.

To run ``tlscli``, you need a Telecom Log Service running somewhere. For
instance you can use ``tao_tls_basic``, the Basic Telecom Log Service
provided with `TAO <http://www.cs.wustl.edu/~schmidt/TAO.html>`_.

Running
=======

When invoking ``tlscli`` you need to specify how to connect to the LogMgr.
The LogMgr is the object to use to access (or create) logs.

This is achieved by specifying an initial reference for the LogMgr, using one
of the three following methods:

* add ``-ORBInitRef LogMgr=corbaname:iiop:1.2@MACHINE:PORT#NAME``
* add ``-ORBInitRef LogMgr=corbaloc:iiop:1.2@MACHINE:PORT/NAME``
* add ``-ORBInitRef LogMgr=IOR:IOR``

where ``MACHINE:PORT`` specify where to find a Telecom Log Service (or
a Name Service for ``corbaname``), and ``NAME`` is the name to use
for the service (or the Name Service for ``corbaname``).

Please read `The corbaloc and corbaname URLs chapter
<http://www.ciaranmchale.com/corba-explained-simply/the-corbaloc-and-corbaname-urls.html>`_
in the great online free book
`CORBA Explained Simply <http://www.ciaranmchale.com/corba-explained-simply/>`_.

Commands
========

Creating a new log (*basic log only*)
-------------------------------------
To create a new log, use ``tlscli create``. This will return the id of the
newly created log.

Querying an existing log
------------------------
* ``list`` will return the id of all logs available from the given LogMgr.
  This is the default command if none is specified
* ``info`` will return information about an existing log, such as size,
  record count and current status
* ``query`` can be used to search for log records matching a given constraint
* ``retrieve`` retrieves a given count of log records before or after the
  specified date

Modifying an existing log
-------------------------
* ``write`` adds a new log record to an existing log
* ``delete`` removes log records matching a given constraint from an existing
  log


For more information on commands, use ``tlscli --help``.
