%define module	Lingua-Preferred
%define version	0.2.4
%define release %mkrel 4

Summary:	Perl extension to choose a language
License:	GPL/Artistic
Name:		perl-%{module}
Version:	%{version}
Release:	%{release}
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:		ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Lingua/%{module}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl(Log::TraceMessages)
BuildRequires:	perl-devel


%description
Often human-readable information is available in more than one language. Which
should you use? This module provides a way for the user to specify possible
languages in order of preference, and then to pick the best language of those
available. Different 'dialects' given by the 'territory' part of the language
specifier (such as en, en_GB, and en_US) are also supported.

Authors:
--------
        Ed Avis <epa98@doc.ic.ac.uk>

%prep
%setup -n %{module}-%{version} -q

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}
make test

%install
%makeinstall DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Lingua/Preferred.pm
%{perl_vendorlib}/auto/Lingua/Preferred/autosplit.ix
%{_mandir}/*/*


